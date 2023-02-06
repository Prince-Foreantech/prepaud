from django.urls import path
from .views import audio
urlpatterns = [
    path('allaudio',audio),
]
