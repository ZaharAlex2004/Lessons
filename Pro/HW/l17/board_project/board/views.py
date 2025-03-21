from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from datetime import timedelta
from django.utils import timezone
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Ad, User, Comment, Contact, UserProfile
from .forms import RegistrationForm, UserProfileForm, CustomPasswordChangeForm
from .services import *
from .serializers import ContactSerializer


def home_view(request: HttpRequest) -> render:
    """
    Просмотр главной страницы
    :param request: HttpRequest
    :return: render
    """
    today = timezone.now()
    return render(request, "board/board.html", {"today": today})


def ad_list_view(request: HttpRequest) -> render:
    """
    Список объявлений с фильтрацией по категории, статусу и пользователю.
    :param request:
    :return: render
    """
    categories = Category.objects.all()
    users = User.objects.all()
    ads = Ad.objects.all()

    if 'category' in request.GET and request.GET['category']:
        ads = ads.filter(category_id=request.GET['category'])

    if 'status' in request.GET and request.GET['status']:
        if request.GET['status'] == 'active':
            ads = ads.filter(is_active=True)
        elif request.GET['status'] == 'inactive':
            ads = ads.filter(is_active=False)

    if 'user' in request.GET and request.GET['user']:
        ads = ads.filter(user_id=request.GET['user'])

    ads = ads.annotate(comment_count=Count('comments'))

    return render(request, 'board/ads_list.html', {
        'ads': ads,
        'categories': categories,
        'users': users,
    })


def ad_detail_view(request: HttpRequest, ad_id: int) -> render:
    """
    Добавить текст комметарии.
    :param request: HttpRequest
    :param ad_id: Идентификатор для добавления
    :return: render
    """
    ad = get_object_or_404(Ad, id=ad_id)
    comments = ad.comments.all()

    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(ad=ad, user=request.user, content=text)

    return render(request, 'board/ads_list.html', {
        'ad': ad,
        'comments': comments,
    })


class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'})


class ContactListView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer()


def base_view(request: HttpRequest) -> render:
    return render(request, "form/base.html")


@login_required
def register_view(request: HttpRequest) -> render:
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, "form/register.html", {'form': form})


@login_required
def edit_profile_view(request: HttpRequest) -> render:
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, "form/edit_profile.html", {'form': form})


@login_required
def change_password_view(request: HttpRequest) -> render:
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, "form/change_password.html", {'form': form})


@login_required
def profile_view(request: HttpRequest) -> render:
    user_profile = request.user.userprofile
    return render(request, "form/profile.html", {'user_profile': user_profile})
