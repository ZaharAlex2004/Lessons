from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='board'),
    path('ads_list/', views.ad_list_view, name='ads_list'),
    path('ads/<int:ad_id>/', views.ad_detail_view, name='ad_detail'),
]
