from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

items: List[Item] = [
    Item(id=1, name="Notebook", description="A simple notebook", price=4.99),
    Item(id=2, name="Pen", description="A blue ink pen", price=1.99),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Item Store!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(existing_item.id == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted = items.pop(index)
            return {"message": f"Deleted item {deleted.name} (ID {deleted.id})"}
    raise HTTPException(status_code=404, detail="Item not found")
