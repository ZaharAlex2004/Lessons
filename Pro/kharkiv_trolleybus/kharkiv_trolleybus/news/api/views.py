import httpx
from django.http import JsonResponse
from rest_framework import viewsets
from news.models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

async def call_fastapi(request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/fastapi/")
    return JsonResponse(response.json())

def api_view(request):
    return JsonResponse({"message": "Welcome to the Django API!"})