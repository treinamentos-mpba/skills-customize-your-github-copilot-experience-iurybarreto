from itertools import count

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas")


class TaskInput(BaseModel):
    title: str
    description: str = ""


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}
next_task_id = count(1)


# TODO: Crie GET /health e retorne um JSON indicando que a API está funcionando.

# TODO: Crie POST /tasks para validar e cadastrar uma tarefa.

# TODO: Crie GET /tasks para listar as tarefas cadastradas.

# TODO: Crie GET /tasks/{task_id}, PUT /tasks/{task_id} e DELETE /tasks/{task_id}.
# Use HTTPException com status 404 quando a tarefa não existir.
