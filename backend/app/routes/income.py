from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.core.dependencies import get_current_user
from app.models.income import Income
from app.models.category import Category
from app.models.user import User
from app.schemas.income import IncomeCreate, IncomeUpdate,IncomeResponse


router = APIRouter(
    prefix="/income",
    tags=["Income"],
)


# Create a new income record
@router.post(
    "/",
    response_model=IncomeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_income(
    income_data: IncomeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Find an income category belonging to the user
    # or a shared income category
    category = db.query(Category).filter(
        Category.id == income_data.category_id,
        Category.type == "income",
        (
            (Category.user_id == current_user.id)
            | (Category.user_id.is_(None))
        ),
    ).first()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income category not found.",
        )

    # Create the income record
    new_income = Income(
        user_id=current_user.id,
        category_id=income_data.category_id,
        amount_minor=income_data.amount_minor,
        source=income_data.source,
        description=income_data.description,
        date_received=income_data.date_received,
    )

    db.add(new_income)
    db.commit()
    db.refresh(new_income)

    return new_income
# Retrieve all income records belonging to the authenticated user
@router.get(
    "/",
    response_model=list[IncomeResponse],
)
def get_income_records(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    income_records = db.query(Income).filter(
        Income.user_id == current_user.id
    ).order_by(
        Income.date_received.desc(),
        Income.id.desc(),
    ).all()

    return income_records
# Retrieve one income record
@router.get(
    "/{income_id}",
    response_model=IncomeResponse,
)
def get_income_record(
    income_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    income_record = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id,
    ).first()

    if income_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income record not found.",
        )

    return income_record
# Update an existing income record
@router.put(
    "/{income_id}",
    response_model=IncomeResponse,
)
def update_income(
    income_id: int,
    income_data: IncomeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Find an income record belonging to the authenticated user
    income_record = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id,
    ).first()

    if income_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income record not found.",
        )

    # Verify that the selected category is valid
    category = db.query(Category).filter(
        Category.id == income_data.category_id,
        Category.type == "income",
        (
            (Category.user_id == current_user.id)
            | (Category.user_id.is_(None))
        ),
    ).first()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income category not found.",
        )

    # Update the income information
    income_record.category_id = income_data.category_id
    income_record.amount_minor = income_data.amount_minor
    income_record.source = income_data.source
    income_record.description = income_data.description
    income_record.date_received = income_data.date_received

    db.commit()
    db.refresh(income_record)

    return income_record
# Delete an existing income record
@router.delete(
    "/{income_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_income(
    income_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Find an income record belonging to the authenticated user
    income_record = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id,
    ).first()

    if income_record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income record not found.",
        )

    db.delete(income_record)
    db.commit()

    return None