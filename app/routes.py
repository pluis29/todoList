from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, database, crud

router = APIRouter()

# banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas da API tasks/*
@router.post("/", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.create_task(db=db, task=task)
    if not db_task:
        raise HTTPException(status_code=500, detail="Error creating task")
    return db_task

@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return db_task 

@router.get("/", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db=db)
    return tasks

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.delete_task(db=db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"message": "Task deleted successfully"}


@router.put("/{task_id}", response_model=schemas.TaskResponse, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    success = crud.update_task(db=db, task_id=task_id, task=task)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return db_task 


@router.patch("/{task_id}/complete", response_model=schemas.TaskResponse)
async def complete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.complete_task(db=db, task_id=task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return db_task 