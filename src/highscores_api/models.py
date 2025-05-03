from datetime import datetime  # <-- import the actual datetime class
from typing import Optional

from sqlmodel import Field, SQLModel


class Score(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    score: float
    kills: int
    time_alive: int
    date: datetime
