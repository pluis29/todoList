from sqlalchemy.orm import Session
from . import models, schemas
from pydantic import ValidationError

def create_task(db: Session, task: schemas.TaskCreate):
    try:
        db_task = models.Task(task=task.task, status=task.status) 
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return True  # Retorna True se a tarefa foi criada com sucesso
    except ValidationError:
        return False
    except Exception:
        return False  # Caso ocorra algum erro, retorna False
    
def get_tasks(db: Session):
    return db.query(models.Task).all()

def complete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        return False
    if db_task:
        db_task.status = True
        db.commit()
        db.refresh(db_task)
    return True

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        if task.task is not None:
            db_task.task = task.task
        if task.status is not None:
            db_task.status = task.status
        db.commit()
        db.refresh(db_task)
        return True
    return False