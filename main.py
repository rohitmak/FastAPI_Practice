from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def items_route(item_id:int):
    return {"message": "Hello, World!", "item_id": item_id}

@app.get("/users/me")
def get_user_me():
    return {"message": "This is me!"}

@app.get("/users/{user_id}")
def get_user_by_id(user_id: str):
    return {"message": f"This is user with id {user_id}!"}

@app.get("/users")
def get_users_01():
    return ["Rohit", "Ishan"]

@app.get("/users")
def get_users_01():
    return ["Virat", "Hardik"]

# Enums

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model_name(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "Computer Vision"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

# Path inside Path Parameters (using Starlette)

@app.get("/files/{file_path:path}")
def get_file_path(file_path: str):
    return {"file_path": file_path}

