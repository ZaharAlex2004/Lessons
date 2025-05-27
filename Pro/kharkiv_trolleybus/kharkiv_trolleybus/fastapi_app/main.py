import jwt
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import WebSocket, WebSocketDisconnect, Depends, HTTPException
from typing import List
from fastapi_app.routers import news
from fastapi_app.database import metadata, engine


app = FastAPI()

active_connections: List[WebSocket] = []

app.include_router(news.router)

metadata.create_all(engine)

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    active_connections.append(websocket)

    await websocket.send_text(f"Hello, {user_id}! You're connected.")

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message from {user_id}: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        await websocket.close()
