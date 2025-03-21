from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('ads_list/', views.ad_list_view, name='ads_list'),
    path('ads/<int:ad_id>/', views.ad_detail_view, name='ad_detail'),
    path('register/', views.register_view, name='register'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('profile/', views.profile_view, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
