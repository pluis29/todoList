from app.schemas import TaskCreate, TaskUpdate
from pydantic import ValidationError
import pytest

def test_task_create_valid():
    task_data = TaskCreate(task="Test Task", status=False)
    assert task_data.task == "Test Task"
    assert task_data.status == False

def test_task_create_invalid():
    with pytest.raises(ValidationError):
        TaskCreate(task=None, status=False)

def test_task_update_valid():
    task_data = TaskUpdate(task="Updated Task", status=True)
    assert task_data.task == "Updated Task"
    assert task_data.status == True

def test_task_update_invalid():
    with pytest.raises(ValidationError):
        TaskUpdate(task="")  
    with pytest.raises(ValidationError):
        TaskUpdate(task="a" * 256)