from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class News(models.Model):
    title = models.CharField(max_length=255)
    sourse = models.CharField(max_length=255)
    date_published = models.DateField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.TextField(blank=True, max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Comment(models.Model):
    post = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username}'

class UploadFiles(models.Model):
    file = models.FileField(upload_to='img/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class PhotoGallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/img/')
    date = models.TextField(blank=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UploadVideoFile(models.Model):
    file = models.FileField(upload_to='video/')
    title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
