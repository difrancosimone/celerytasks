from celery import Celery

app = Celery('tasks', backend='redis://localhost/0', broker='redis://localhost/0')

@app.task
def add(x, y):
    return x + y

@app.task
def simpleecho(string):
    return string