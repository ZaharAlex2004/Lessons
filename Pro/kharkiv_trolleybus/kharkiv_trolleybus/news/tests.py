import pytest
import json

from datetime import date
from django.test import TestCase
from django.http import HttpResponse
from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from .ws.consumers import NewsConsumer
from .tasks import send_registration_email
from .models import *
from django.contrib.auth import get_user_model

def test_celery_task(request):
    send_registration_email.delay('test@example.com')
    return HttpResponse("Email sent to test@example.com")


@pytest.mark.asyncio
async def test_news_consumer():
    # Создаем пользователя для теста
    user = get_user_model().objects.create_user(username='testuser', password='password')

    # Создаем соединение через WebSocket
    communicator = WebsocketCommunicator(NewsConsumer.as_asgi(), f"/ws/{user.id}/")

    # Ожидаем подключения
    connected, subprotocol = await communicator.connect()
    assert connected

    # Отправляем сообщение через WebSocket
    await communicator.send_json_to({"message": "Test message"})

    # Получаем ответ от WebSocket
    response = await communicator.receive_json_from()
    assert response == {"response": "Test message"}

    # Закрываем соединение
    await communicator.disconnect()


class NewsModelTest(TestCase):

    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username="testuser", password="password")

        # Создаем новость
        self.news_item = News.objects.create(
            title="Тестовая новость",
            sourse="Test Source",
            date_published=date.today(),
            content="Тестовый контент новости.",
            author=self.user
        )

    def test_news_creation(self):
        self.assertEqual(self.news_item.title, "Тестовая новость")
        self.assertEqual(self.news_item.sourse, "Test Source")
        self.assertEqual(self.news_item.author.username, "testuser")

    def test_news_str_method(self):
        self.assertEqual(str(self.news_item), "Тестовая новость")

    def test_news_content(self):
        self.assertEqual(self.news_item.content, "Тестовый контент новости.")