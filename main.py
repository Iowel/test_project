from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def ping():
    return 'pong'


@app.get('/hello')
def print_hello():
    return {'msg': 'Hello, world!'}

@app.get('/world')
def print_world():
    return {'msg': 'Hello, world!'}