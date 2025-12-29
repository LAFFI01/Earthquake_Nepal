from fastapi import FastAPI
from API.routers import prediction

app = FastAPI()

app.include_router(prediction.router)
@app.get("/")
async def root():
    return {"message": "I am alive!"}