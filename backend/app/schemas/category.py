from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# Accepted category types
CategoryType = Literal["income", "expense"]


# Schema for creating a category
class CategoryCreate(BaseModel):
    name: str = Field(min_length=1)
    type: CategoryType


# Schema for returning category information
class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int | None
    name: str
    type: CategoryType
    created_at: datetime