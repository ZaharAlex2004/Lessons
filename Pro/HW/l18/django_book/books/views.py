import django_filters
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .models import Book
from .serializers import BookSerializer


class BookFilter(django_filters.FilterSet):
    """
    Класс фильтрации книг.
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        """
        Класс Meta.
        """
        model = Book
        fields = ['title', 'author', 'genre', 'publication_year']


class BookPagination(PageNumberPagination):
    """
    Класс страницы книги.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookViewSet(viewsets.ModelViewSet):
    """
    Класс просмотра книги.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = (DjangoFilterBackend,)
    ordering_fields = ['title', 'author', 'publication_year']
    ordering = ['title']
    filterset_class = BookFilter
    filterset_fields = ['author', 'genre', 'publication_year']

    def get_permissions(self) -> [permissions.IsAuthenticated()]:
        """
        Получение разрешения.
        :return: [permissions.IsAuthenticated()]
        """
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


def books_view(request: HttpRequest) -> JsonResponse:
    """
    Просмотр книги.
    :param request: HttpRequest/
    :return: JsonResponse(serializer.data, safe=False)
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)
