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
from fastapi_app.main import app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kharkiv_trolleybus.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter({
        path("ws/<str:user_id>", NewsConsumer.as_asgi()),
    }),
    "fastapi": app,
})