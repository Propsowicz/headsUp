from django.urls import re_path
from .consumers import HomePageLobby, LobbyRoom

websocket_urlpatterns = [
    re_path(r'ws/home-page/$', HomePageLobby.as_asgi()),
    re_path(r'ws/(?P<room_name>\w+)/lobby/$', LobbyRoom.as_asgi()),
]