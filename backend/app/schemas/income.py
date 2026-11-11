from datetime import date, datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints


# Text validation
IncomeSource = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1),
]

IncomeDescription = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1),
]


# Schema for creating income
class IncomeCreate(BaseModel):
    category_id: int = Field(gt=0)
    amount_minor: int = Field(gt=0)
    source: IncomeSource
    description: IncomeDescription | None = None
    date_received: date


# Schema for updating income
class IncomeUpdate(BaseModel):
    category_id: int = Field(gt=0)
    amount_minor: int = Field(gt=0)
    source: IncomeSource
    description: IncomeDescription | None = None
    date_received: date


# Schema for returning income information
class IncomeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    category_id: int
    amount_minor: int
    source: str
    description: str | None
    date_received: date
    created_at: datetime