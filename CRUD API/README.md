# Task CRUD API

A beginner-friendly **CRUD API** for managing to-do tasks, built with **Python, FastAPI, and Uvicorn**.

The API supports the four basic CRUD operations:

- **Create** a task
- **Read** all tasks or one task
- **Update** a task
- **Delete** a task

The project uses an **in-memory Python list**, so newly created or updated tasks disappear when the server is restarted. No database is used in this assignment.

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI
- Git and GitHub

## Project Structure

```text
CRUD API/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Open the project folder

```powershell
cd "C:\Users\priva\Desktop\CRUD API"
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the dependencies

```powershell
python -m pip install fastapi "uvicorn[standard]"
```

Alternatively, when `requirements.txt` is available:

```powershell
python -m pip install -r requirements.txt
```

## Run the Server

```powershell
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| HTTP Method | Endpoint | Description | Success Status |
|---|---|---|---|
| GET | `/` | Display API information | `200 OK` |
| GET | `/health` | Check whether the server is running | `200 OK` |
| GET | `/tasks` | Return all tasks | `200 OK` |
| GET | `/tasks/{task_id}` | Return one task by ID | `200 OK` |
| POST | `/tasks` | Create a new task | `201 Created` |
| PUT | `/tasks/{task_id}` | Update an existing task | `200 OK` |
| DELETE | `/tasks/{task_id}` | Delete an existing task | `204 No Content` |

## Task Format

Each task contains:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

## Example Requests

### Get all tasks

```powershell
curl.exe -i http://127.0.0.1:8000/tasks
```

### Get one task

```powershell
curl.exe -i http://127.0.0.1:8000/tasks/1
```

### Create a task

```powershell
curl.exe -i -X POST http://127.0.0.1:8000/tasks `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Buy milk\"}"
```

Expected status:

```text
HTTP/1.1 201 Created
```

Example response:

```json
{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

### Update a task

```powershell
curl.exe -i -X PUT http://127.0.0.1:8000/tasks/4 `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Buy oat milk\",\"done\":true}"
```

### Delete a task

```powershell
curl.exe -i -X DELETE http://127.0.0.1:8000/tasks/4
```

Expected status:

```text
HTTP/1.1 204 No Content
```

## Error Handling

The API uses these status codes:

| Status Code | Meaning |
|---|---|
| `200 OK` | A read or update operation succeeded |
| `201 Created` | A new task was created |
| `204 No Content` | A task was deleted |
| `400 Bad Request` | The request body was missing or invalid |
| `404 Not Found` | The requested task ID does not exist |

Example error:

```json
{
  "error": "Task 99 not found"
}
```

## Swagger UI

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Use **Try it out** to test the complete CRUD cycle.

Add your screenshot to the project, for example:

```text
docs/swagger-ui.png
```

Then display it here:

```markdown
![Swagger UI](docs/swagger-ui.png)
```

## In-Memory Storage

This project stores tasks inside a Python list rather than a database.

When the server stops, the program's memory is cleared. Therefore, tasks created during runtime disappear after restarting the server. A database will be used in a later project to make the data persistent.

## Git Commit Stages

Suggested meaningful commits:

```text
Stage 0: hello server
Stage 1: root and health endpoints
Stage 2: read endpoints with 404
Stage 3: create with validation
Stage 4: full CRUD
Stage 5: Swagger UI
Stage 6: publish and docs
```
