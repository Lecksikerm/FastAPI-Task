from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        title=task.title,
        description=task.description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_task(db: Session, task_id: int, data: TaskUpdate):
    task = get_task(db, task_id)
    if not task:
        return None

    task.title = data.title
    task.description = data.description
    task.completed = data.completed

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task
