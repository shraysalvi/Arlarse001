from django.urls import path, include
from .views import event_page
urlpatterns = [
    path("", event_page),
]