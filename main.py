from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# def items_route(item_id:int):
#     return {"message": "Hello, World!", "item_id": item_id}

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

# Query Parameters

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit] # slice the list [include:exclude]

# Optional Parameters

# @app.get("/items/{item_id}")
# def get_item(item_id: int, q: str | None = None): # or also q: Union[str, None]
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     return item

from typing import Union

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q :
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a long description"})
    return item

# Multiple path and query parameters
# You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.

# And you don't have to declare them in any specific order.

# They will be detected by name:

@app.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a long description"})
    return item

# Required Query Parameters

@app.get("/item/{item_id}")
def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item