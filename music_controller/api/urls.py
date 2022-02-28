from django.urls import path
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
]