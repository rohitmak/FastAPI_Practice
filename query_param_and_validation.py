# Query Parameters and String Validations

from fastapi import FastAPI, Query
from typing import Union, Annotated

app = FastAPI()

# Using Annotated (use this one) ↓

@app.get("/items/")
def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# old way (without Annotated, avoid it) ↓ 

# @app.get("/items/")
# def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results