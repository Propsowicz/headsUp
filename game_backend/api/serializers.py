from rest_framework import serializers   
from game_backend.models import GameRoom
from player.models import Player


class GameRoomSerializer(serializers.ModelSerializer):    
    class Meta:
        model = GameRoom
        fields = '__all__'


def CustomRoomSerializer(game_room):
    return_list = []
    for i in range(game_room.count()):        
        return_list.append({'id': game_room[i].id, 
                            'is_started': game_room[i].is_started, 
                            'is_ended': game_room[i].is_ended,
                            'players': 
                            [{'nickname': j.nickname, 'player_id': j.id, 
                            'is_host': j.is_host, 'score': j.score} for j in game_room[i].player.all()],
                            })
    return return_list