from django.urls import path
from .views import GameRoomHostAPI, JoinRommAPI

urlpatterns = [
    path('get-host/<int:id>/', GameRoomHostAPI.as_view()),
    path('join-room/<int:id>/', JoinRommAPI.as_view()),

]
