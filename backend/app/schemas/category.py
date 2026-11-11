from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, StringConstraints


# Accepted category types
CategoryType = Literal["income", "expense"]

# Category names must contain at least one non-whitespace character
CategoryName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1),
]


# Schema for creating a category
class CategoryCreate(BaseModel):
    name: CategoryName
    type: CategoryType


# Schema for updating a category
class CategoryUpdate(BaseModel):
    name: CategoryName
    type: CategoryType


# Schema for returning category information
class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int | None
    name: str
    type: CategoryType
    created_at: datetime