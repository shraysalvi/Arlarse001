from django.urls import path, include
from .views import event_page, privacy_page

urlpatterns = [
    path("", event_page),
    path("privacy", privacy_page),
]
