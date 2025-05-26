from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:client_id>/', consumers.NewsConsumer.as_asgi(), name='ws-client'),
]