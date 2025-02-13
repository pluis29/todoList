from app import crud, schemas
from app.models import Task

# Testes para create_task
def test_create_task_valid(db_session):
    task_data = schemas.TaskCreate(task="Test Task", status=False)
    result = crud.create_task(db=db_session, task=task_data)
    assert result is not None
    task_in_db = db_session.query(Task).first()
    assert task_in_db.task == "Test Task"
    assert task_in_db.status is False


def test_create_task_invalid(db_session):
    task1 = Task(task="Task 1", status=False)
    result = crud.create_task(db=db_session, task=task1.id)
    assert result is None

def test_get_tasks(db_session):
    task1 = Task(task="Task 1", status=False)
    task2 = Task(task="Task 2", status=True)
    db_session.add(task1)
    db_session.add(task2)
    db_session.commit()
    tasks = crud.get_tasks(db=db_session)
    assert len(tasks) == 2
    assert tasks[0].task == "Task 1"
    assert tasks[1].task == "Task 2"

# Testes para complete_task
def test_complete_task_valid(db_session):
    task = Task(task="Test Task", status=False)
    db_session.add(task)
    db_session.commit()
    result = crud.complete_task(db=db_session, task_id=task.id)
    assert result is True
    completed_task = db_session.query(Task).filter(Task.id == task.id).first()
    assert completed_task.status is True

def test_complete_task_invalid(db_session):
    result = crud.complete_task(db=db_session, task_id=999)
    assert result is False

# Testes para delete_task
def test_delete_task_valid(db_session):
    task = Task(task="Test Task", status=False)
    db_session.add(task)
    db_session.commit()
    result = crud.delete_task(db=db_session, task_id=task.id)
    assert result is True
    task_in_db = db_session.query(Task).filter(Task.id == task.id).first()
    assert task_in_db is None

def test_delete_task_invalid(db_session):
    result = crud.delete_task(db=db_session, task_id=999)
    assert result is False

# Testes para update_task
def test_update_task_valid(db_session):
    task = Task(task="Test Task", status=False)
    db_session.add(task)
    db_session.commit()
    update_data = schemas.TaskUpdate(task="Updated Task", status=True)
    result = crud.update_task(db=db_session, task_id=task.id, task=update_data)
    assert result is True
    updated_task = db_session.query(Task).filter(Task.id == task.id).first()
    assert updated_task.task == "Updated Task"
    assert updated_task.status is True

def test_update_task_invalid(db_session):
    update_data = schemas.TaskUpdate(task="Updated Task", status=True)
    result = crud.update_task(db=db_session, task_id=999, task=update_data)
    assert result is False