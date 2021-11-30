from fastapi import FastAPI
import uvicorn
from typing import Dict
from typing import Any

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/fruit")
async def fruit():
    return {
        "fruit": "Watermelon",
        "car": "yugo"
    }


@app.post("/list_fruit")
async def list_fruit(item: Dict[Any, Any] = None):
    return item


if __name__ == "__main__":
    uvicorn.run("fastapi_sample:app", host="0.0.0.0", port=8080, reload=True)
