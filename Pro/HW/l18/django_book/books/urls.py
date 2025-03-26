from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import BookViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Book API",
      default_version='v1',
      description="API для керування книгами",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@bookapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger    -docs'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
