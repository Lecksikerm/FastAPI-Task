# FastAPI Task Manager

## Overview

A simple Task Manager API built with **FastAPI**, **SQLAlchemy**, and **SQLite**, demonstrating full CRUD operations.

---

## Features

* Create, read, update, and delete tasks
* Swagger UI API documentation
* Pydantic models for request validation
* SQLite database via SQLAlchemy ORM
* Easy to extend for authentication or PostgreSQL

---

## Technology Stack

* Python 3.12+
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Uvicorn
* python-dotenv

---

## Installation

1. Clone the repository:

```
git clone https://github.com/Lecksikerm/fastapi-task.git
cd fastapi-task
```

2. Create and activate virtual environment:

```
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

```
uvicorn main:app --reload
```

* Server URL: `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

### Root

* `GET /` - Returns API status

```json
{
  "message": "FastAPI Task Manager is running!"
}
```

### Tasks

#### Get all tasks

* `GET /tasks`

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the CRUD tutorial",
    "completed": false
  }
]
```

#### Get single task

* `GET /tasks/{task_id}`

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete the CRUD tutorial",
  "completed": false
}
```

#### Create a task

* `POST /tasks`

```json
{
  "title": "Learn FastAPI",
  "description": "Complete the CRUD tutorial"
}
```

* Response:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete the CRUD tutorial",
  "completed": false
}
```

#### Update a task

* `PUT /tasks/{task_id}`

```json
{
  "title": "Learn FastAPI Properly",
  "description": "Complete CRUD and Swagger UI",
  "completed": true
}
```

#### Delete a task

* `DELETE /tasks/{task_id}`

```json
{
  "deleted": true
}
```

---

## Notes

* Tasks are created with `completed = false` by default.
* `/favicon.ico` 404 is normal in browsers.
* Pydantic v2 users may see `orm_mode` warning; use `model_config = {"from_attributes": True}` to fix.

---

## References

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
* [Pydantic Documentation](https://docs.pydantic.dev/)

