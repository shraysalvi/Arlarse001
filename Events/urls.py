from django.urls import path, include
from .views import event_page, privacy_page, comming_soon, _help

urlpatterns = [
    path("", event_page),
    path("privacy", privacy_page),
    path("help", _help),
    path("coming_soon", comming_soon),
]
