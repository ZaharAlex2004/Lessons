from datetime import date

from django.http import request, JsonResponse, HttpResponse, HttpRequest
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from typing import Any
from rest_framework import viewsets
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .tasks import send_registration_email, send_promotional_email
from .forms import *
from .models import *
from .serializers import *

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

def main_page(request):
    today = date.today()
    news = News.objects.all().order_by('-date_published')
    files = UploadFiles.objects.all().order_by('-uploaded_at')
    return render(request, 'kharkiv_trolleybus/main_page.html', {'today': today, 'news': news, 'title':'Харьковский троллейбус - главная страница', 'files': files})

def chrome_devtools_dummy(request):
    return JsonResponse({}, status=200)

def register(request):
    """Регистрация нового пользователя и отправка имейлов."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            send_mail(
                'Харьковский троллейбус',
                'Благодарим вас за регистрацию!',
                'zaharalex04@gmail.com',
                [user.email],
                fail_silently=False,
            )
            return redirect('main')
    else:
        form = RegistrationForm()
    return render(request, 'kharkiv_trolleybus/register.html', {'form': form, 'title':'Регистрация'})

def user_login(request: HttpRequest) -> render:
    """
    Вход
    :param request: HttpRequest
    :return: render
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return render(request, 'kharkiv_trolleybus/login.html', {'form': form, 'error': 'Invalid username or password!', 'title':'Логин'})
    else:
        form = UserLoginForm()

    return render(request, 'kharkiv_trolleybus/login.html', {'form': form, 'title':'Логин'})

def user_logout(request):
    logout(request)
    return redirect('main')

def depo_views(request):
    return render(request, 'kharkiv_trolleybus/depo.html', {'title':'Депо'})

def depo_2_views(request):
    return render(request, 'kharkiv_trolleybus/depo_2.html', {'title':'Троллейбусное депо №2'})

def depo_3_views(request):
    return render(request, 'kharkiv_trolleybus/depo_3.html', {'title':'Троллейбусное депо №3'})

def depo_saltov_views(request):
    return render(request, 'kharkiv_trolleybus/depo_saltov.html', {'title':'Салтовское трамвайное депо'})

def route_views(request):
    return render(request, 'kharkiv_trolleybus/route.html', {'title':'Маршруты'})

def history_view(request):
    return render(request, 'kharkiv_trolleybus/history.html', {'title':'История'})

def video_view(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video')
    else:
        form = UploadVideoForm()
    files = UploadVideoFile.objects.all()
    return render(request, 'kharkiv_trolleybus/video.html', {'title':'Видео', 'form': form, 'files': files})

def image_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image')
    else:
        form = UploadFileForm()
    files = UploadFiles.objects.all()
    return render(request, 'kharkiv_trolleybus/image.html', {'title': 'Фотогалерея', 'form': form, 'files': files})

def upload_imgs(request):
    return render(request, 'kharkiv_trolleybus/upload_file.html', {'title': 'Разное'})

def different_view(request):
    return render(request, 'kharkiv_trolleybus/different.html', {'title':'Разное'})

def models_view(request):
    return render(request, 'kharkiv_trolleybus/models.html', {'title':'Подвижной состав'})

def news_view(request):
    news = News.objects.all()
    return render(request, 'kharkiv_trolleybus/news.html', {'news': news, 'title':'Новости'})

@login_required
def create_news_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'kharkiv_trolleybus/create_news.html', {'form': form, 'title':'Создать статью'})

def schema_view(request):
    return render(request, 'kharkiv_trolleybus/schema.html', {'title':'Схемы'})

def facts_view(request):
    return render(request, 'kharkiv_trolleybus/facts.html', {'title':'Факты'})

def news_detail(request, pk: Any):
    post = get_object_or_404(News, pk=pk)
    comments = post.comments.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "news_group",
                    {
                        "type": "chat_message",
                        "message": f"New comment on post {post.title}"
                    }
                )
                return redirect('news_detail', pk=post.pk)
        else:
            return redirect('login')

    else:
        form = CommentForm()

    return render(request, 'kharkiv_trolleybus/news_detail.html', {'post': post, 'comments': comments, 'form': form, 'title':'Новости'})