"""
ASGI config for kharkiv_trolleybus project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from news.ws.consumers import NewsConsumer
from news.ws import routing
#from news.routing import websocket_urlpatterns

app = FastAPI()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kharkiv_trolleybus.settings')

active_connections: List[WebSocket] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI!"}

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter({
        path("ws/<str:user_id>", NewsConsumer.as_asgi()),
    }),
})