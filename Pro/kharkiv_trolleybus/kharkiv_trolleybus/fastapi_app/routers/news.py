from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from fastapi_app.schemas import News, NewsCreate, UserCreate
from fastapi_app.database import SessionLocal, get_db
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_app import crud
from fastapi_app.services import send_data_to_django

router = APIRouter()

def fake_background_task(message: str):
    import time
    time.sleep(5)
    print(f"Background: {message}")

@router.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI!"}

@router.get("/from-django")
async def get_data():
    data = await send_data_to_django
    return {"django_data" : data}

@router.get("/fastapi/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@router.post("/users/")
async def create_user(user: UserCreate):
    return await crud.create_user(user)

@router.get("/users/")
async def list_users():
    return await crud.get_users()

@router.post("/news/")
async def create_news(news: NewsCreate, background_tasks: BackgroundTasks):
    background_tasks.add_task(fake_background_task, f"New post: {news.title}")
    return await crud.create_news(news)

@router.patch("/news/{news_id}")
async def update_news(news_id: int, title: str):
    return await crud.patch_news(news_id, title)

@router.delete("/news/{news_id}")
async def delete_news(news_id: int):
    return await crud.delete_news(news_id)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()