from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def read_items():
    return {"items": ["item3", "item4"]}