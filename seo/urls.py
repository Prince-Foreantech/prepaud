from django.urls import path
from .views import discription

urlpatterns = [
    path("blogdiscription",discription),
]
