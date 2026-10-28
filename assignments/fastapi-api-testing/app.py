from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas")


class TaskInput(BaseModel):
    title: str
    description: str = ""


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput) -> Task:
    task_id = max(tasks, default=0) + 1
    task = Task(id=task_id, **task_input.model_dump())
    tasks[task_id] = task
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    task = Task(id=task_id, **task_input.model_dump())
    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    del tasks[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
