from pydantic import BaseModel, Field, model_validator
from typing import Optional

class TaskCreate(BaseModel):
    task: str = Field(..., min_length=1, max_length=255, description="Descrição da tarefa")
    status: Optional[bool] = Field(default=False, description="Status de conclusão da tarefa")
    
    @model_validator(mode='before')
    def set_default_status(cls, values):
        if values.get('status') is None:
            values['status'] = False
        return values
    @model_validator(mode='before')
    def check_task(cls, values):
        task = values.get('task')
        if task is None or task.strip() == "":
            raise ValueError("O campo 'task' não pode ser None ou uma string vazia.")
        return values
    
class TaskUpdate(BaseModel):
    task: Optional[str] = Field(None, min_length=1, max_length=255, description="Descrição da tarefa")
    status: Optional[bool] = Field(None, description="Status de conclusão da tarefa")

class TaskResponse(BaseModel):
    id: int
    task: str
    status: bool

    class Config:
        orm_mode = True