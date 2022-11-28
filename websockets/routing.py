from django.urls import re_path
from .consumers import HomePageLobby

websocket_urlpatterns = [
    re_path(r'ws/home-page/$', HomePageLobby.as_asgi()),
    # re_path(r'ws/home-page/(?P<room_name>\w+)/$', HomePageLobby.as_asgi()),
]