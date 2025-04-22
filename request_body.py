# Request body is needed to send data to API 

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float    
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
        
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    
    return item_dict

# Request body + path parameters

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}

# Request body + path + query parameters

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    res = {"item_id": item_id, **item.model_dump()}
    if q:
        res.update({"q":q})
    return res