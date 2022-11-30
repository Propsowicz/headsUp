
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('player/api/', include('player.api.urls')),
    path('game_backend/api/', include('game_backend.api.urls')),
]
