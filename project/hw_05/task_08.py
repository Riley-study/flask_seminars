# Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.
from random import choice
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from uvicorn import run as unicorn_run

app = FastAPI()
templates = Jinja2Templates(directory="templates")

ID = 0
TITLES = ["Подготовить презентацию",
          "Сделать покупки",
          "Провести занятие по программированию",
          "Забрать детей"]
DESCRIPTIONS = ["Подготовить презентацию для встречи с клиентом",
                "Купить продукты и товары для дома",
                "Подготовить урок и провести занятие для учеников",
                "Забрать детей из школы"]
STATUS = ['выполнена', 'не выполнена']
tasks = []


class TaskIn(BaseModel):
    title: str
    description: str
    status: str


class Task(TaskIn):
    id: int


def add_new_tasks(num: int = 4):
    global ID
    for i in range(num):
        ID += 1
        new_task = Task(id=ID, title=TITLES[i], description=DESCRIPTIONS[i], status=choice(list(STATUS)))
        tasks.append(new_task)
    return tasks


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'title': 'Главная'})


@app.get('/tasks/', response_model=list[Task])
async def get_tasks():
    if len(tasks) == 0:
        add_new_tasks(2)
    return tasks


@app.get('/tasks/{id}', response_model=Task)
async def get_task(id: int):
    for task in tasks:
        if task.id == id:
            searching_task = task
            return searching_task
    raise HTTPException(status_code=404, detail='Task not found')


@app.post('/tasks/', response_model=Task)
async def create_task(task_in: TaskIn):
    global ID
    ID += 1
    new_task = Task(id=ID, title=task_in.title, description=task_in.description, status=task_in.status)
    tasks.append(new_task)
    return new_task


@app.put('/tasks/{id}', response_model=Task)
async def update_task(id: int, task_in: TaskIn):
    for task in tasks:
        if task.id == id:
            task.title = task_in.title
            task.description = task_in.description
            task.status = task_in.status
            return task
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete('/tasks/{id}', response_model=dict)
async def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            searching_task = task
            tasks.remove(searching_task)
            return {'message': 'Successful task deletion'}
    raise HTTPException(status_code=404, detail='Task not found')


if __name__ == '__main__':
    unicorn_run('task_08:app', host='127.0.0.1', port=8000, reload=True)
