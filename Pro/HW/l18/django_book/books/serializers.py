from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Класс BookSerializer
    """
    class Meta:
        """
        Класс Meta
        """
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'publication_year', 'created_at']
