from django.urls import path, re_path
from . import views
from .views import ContactView, ServiceView


urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("service/", ServiceView.as_view(), name="service"),
    path("event/", views.event_view, name="event"),
    path("post/", views.post_view, name="post"),
    path("profile/", views.profile_view, name="profile"),
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post'),
    re_path(r'^profile/(?P<username>[a-zA-Z]+)/$', views.profile_view, name='profile'),
    re_path(r'^event/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.event_view, name='event'),
]
