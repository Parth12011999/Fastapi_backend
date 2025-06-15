from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from src.entities.todo import Priority


class TodoBase(BaseModel):
    description: str
    due_date: Optional[datetime] = None
    priority: Priority = Priority.Medium


class TodoCreate(TodoBase):
    pass


# ✅ New schema with all fields optional
class TodoUpdate(BaseModel):
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[Priority] = None


class TodoResponse(TodoBase):
    id: UUID
    is_completed: bool
    completed_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
