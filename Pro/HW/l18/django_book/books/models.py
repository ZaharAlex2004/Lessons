from django.db import models


class Book(models.Model):
    """
    Класс модели Book.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Вывод строки.
        :return:
        """
        return self.title
