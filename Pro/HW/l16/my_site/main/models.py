from django.db import models


class Service(models.Model):
    name = models.TextField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.price}"
