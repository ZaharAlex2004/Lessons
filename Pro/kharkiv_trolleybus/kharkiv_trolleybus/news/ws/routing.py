from django.urls import re_path
from news.ws.consumers import NewsConsumer

websocket_urlpatterns = [
    re_path(r"ws/(?P<user_id>\d+)/$", NewsConsumer.as_asgi()),
]