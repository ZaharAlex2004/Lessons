from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import *

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', views.main_page, name='main'),
    path('api/', include(router.urls)),
    path('depo/', views.depo_views, name='depo'),
    path('depo_2/', views.depo_2_views, name='depo_2'),
    path('depo_3/', views.depo_3_views, name='depo_3'),
    path('depo_saltov/', views.depo_saltov_views, name='depo_saltov'),
    path('register/', views.register, name='register'),
    path('route/', views.route_views, name='route'),
    path('history/', views.history_view, name='history'),
    path('video/', views.video_view, name='video'),
    path('image/', views.image_view, name='image'),
    path('different/', views.different_view, name='different'),
    path('models/', views.models_view, name='models'),
    path('news/', views.news_view, name='news'),
    path('schema/', views.schema_view, name='schema'),
    path('news/create_news/', views.create_news_view, name='create_news'),
    path('news/<int:pk>', views.news_detail, name='news_detail'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('facts/', views.facts_view, name='facts'),
    path('upload_img/', views.upload_imgs, name='upload_img'),
    path('.well-known/appspecific/com.chrome.devtools.json', chrome_devtools_dummy),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)