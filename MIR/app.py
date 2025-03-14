from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from missions import router as mission_router  # Import the mission routes
from mission_queue import router as mission_queue_router  # Import the mission routes
from registers import router as registers_router  # Import the mission routes
from status import router as status_router  # Import the mission routes


app = FastAPI()
app.include_router(mission_router)
app.include_router(mission_queue_router)
app.include_router(registers_router)
app.include_router(status_router)

# Global shared state
app.state.shared_state = {"base": {"state": 3}}

# Define a model for input data
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def read_root():
    return {"message": "REST API FOR MIR", "documenation": "Go to 193.10.203.23:8000/docs for documentation"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in fake_items_db:
        return {"item_id": item_id, "item": fake_items_db[item_id]}
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(item: Item):
    item_id = len(fake_items_db) + 1  # Simple incrementing ID
    fake_items_db[item_id] = item
    return {"item_id": item_id, "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in fake_items_db:
        fake_items_db[item_id] = item
        return {"message": "Item updated", "item_id": item_id, "item": item}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_items_db:
        del fake_items_db[item_id]
        return {"message": "Item deleted", "item_id": item_id}
    return {"error": "Item not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

