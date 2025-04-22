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