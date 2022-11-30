from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CustomRoomSerializer, GameRoomSerializer
from game_backend.models import GameRoom
from player.models import Player
import json


class GameRoomAPI(APIView):
    def get(self, request, id):
        data = GameRoom.objects.get(id=id)
        serializer = CustomRoomSerializer
        return Response()

class JoinRommAPI(APIView):
    def post(self, request, id):
        player_id = json.loads(request.body)['player_id']
        print(player_id)
        game_room = GameRoom.objects.get(id=id)
        game_room.player.add(Player.objects.get(id=player_id))
        game_room.save()
        return Response('200')

class GameRoomHostAPI(APIView):
    def get(self, request, id):
        host_id = GameRoom.objects.get(id=id).player.all().filter(is_host=True)[0].id
        return Response(host_id)