from pydantic import BaseModel, Field
from typing import Optional

class TaskCreate(BaseModel):
    task: str = Field(..., min_length=1, max_length=255, description="Descrição da tarefa")
    status: Optional[bool] = Field(default=False, description="Status de conclusão da tarefa")

class TaskUpdate(BaseModel):
    task: Optional[str] = Field(None, min_length=1, max_length=255, description="Descrição da tarefa")
    status: Optional[bool] = Field(None, description="Status de conclusão da tarefa")

class TaskResponse(BaseModel):
    id: int
    task: str
    status: bool

    class Config:
        orm_mode = True