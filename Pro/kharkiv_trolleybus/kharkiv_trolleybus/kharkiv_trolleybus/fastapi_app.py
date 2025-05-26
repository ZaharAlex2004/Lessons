import jwt
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import WebSocket, WebSocketDisconnect, Depends, HTTPException
from typing import List
from news.database import SessionLocal

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

active_connections: List[WebSocket] = []

class NewsItem(BaseModel):
    title: str
    content: str
    author: str
    created_at: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI!"}

@app.post("/news/")
def create_news(news_item: NewsItem):
    return {"message": "News item created", "data": news_item}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    await websocket.send_text(f"Hello, {user_id}!")
    await websocket.close()
