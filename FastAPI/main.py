from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Details(BaseModel):
    name: str
    subject: str
    id: int


@app.get('/')
def sample_api():
    return "sample api"


# query parameter
@app.post('/products')
def product(details: Details):
    return f"This is my product id {details.id},name is {details.name}"
