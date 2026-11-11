from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.category import Category
from app.models.user import User
from app.core.dependencies import get_current_user
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


# Create a new personal category
@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Check for an existing personal category with the same name and type
    existing_category = db.query(Category).filter(
        Category.user_id == current_user.id,
        Category.name == category_data.name.strip(),
        Category.type == category_data.type,
    ).first()

    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You already have a category with this name and type.",
        )

    # Create the category for the authenticated user
    new_category = Category(
        user_id=current_user.id,
        name=category_data.name.strip(),
        type=category_data.type,
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


# Retrieve shared and personal categories
@router.get(
    "/",
    response_model=list[CategoryResponse],
)
def get_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    categories = db.query(Category).filter(
        (Category.user_id == current_user.id)
        | (Category.user_id.is_(None))
    ).order_by(Category.id.asc()).all()

    return categories
# Update an existing personal category
@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Find a category belonging to the authenticated user
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == current_user.id,
    ).first()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found.",
        )

    # Normalize the category name
    new_name = category_data.name.strip()

    if not new_name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Category name cannot be empty.",
        )

    # Check for another personal category with the same name and type
    existing_category = db.query(Category).filter(
        Category.user_id == current_user.id,
        Category.name == new_name,
        Category.type == category_data.type,
        Category.id != category_id,
    ).first()

    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You already have a category with this name and type.",
        )

    # Prevent changing the type of a category already in use
    if category.type != category_data.type:
        if (
            category.incomes
            or category.expenses
            or category.budgets
            or category.planned_expenses
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Cannot change the type of a category that is already in use.",
            )

    # Update the existing category
    category.name = new_name
    category.type = category_data.type

    db.commit()
    db.refresh(category)

    return category
# Delete an existing personal category
@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Find a category belonging to the authenticated user
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == current_user.id,
    ).first()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found.",
        )

    # Check whether the category is being used
    if (
        category.incomes
        or category.expenses
        or category.budgets
        or category.planned_expenses
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "Cannot delete this category because it is "
                "being used by existing financial records."
            ),
        )

    # Delete the category
    db.delete(category)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Could not delete this category because it is in use.",
        )