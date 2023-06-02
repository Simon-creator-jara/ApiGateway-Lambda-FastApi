from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/hello")
def hello_world():
    return {"Hello": "World"}

@app.get("/example")
def example():
    return {"example": "this is an example"}


@app.get("/example/we-did-it")
def example():
    return {"winner": "it works"}

handler = Mangum(app)