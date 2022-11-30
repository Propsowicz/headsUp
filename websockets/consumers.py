from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from player.models import Player
from game_backend.models import GameRoom
from game_backend.api.serializers import GameRoomSerializer, CustomRoomSerializer

class HomePageLobby(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):  
        self.room_group_name = 'lobby'
        data = await self.render_all_rooms()
        await self.accept()

        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name,
        )
        
        await self.send(json.dumps(data)) 


    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        if text_data_json['header'] == 'CREATE':
            await self.create_new_lobby_room(text_data_json)
        data = await self.render_all_rooms()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'lobby_rooms',
                'data': data
            },
        )

    async def lobby_rooms(self, event):
        data = event['data']
        await self.send(json.dumps(data))

    @database_sync_to_async
    def render_all_rooms(self):
        data = GameRoom.objects.prefetch_related('player').filter(is_started=False).filter(is_ended=False)
        serializer = CustomRoomSerializer(data)
        return serializer

    @database_sync_to_async
    def create_new_lobby_room(self, msg):
        player = Player.objects.get(id=msg['host_id'])
        player.is_host = True
        player.save()
        game_room = GameRoom.objects.create()
        game_room.player.add(player)
        game_room.save()     

class LobbyRoom(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):  
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'lobby_room_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        try:
            player_nickname = await self.get_player_nickname(text_data_json['user'])
        except:
            player_nickname = 'Anonimowy'

        if text_data_json['header'] == 'CONNECTED':
            answer_msg = f"{player_nickname} dołączył/a do pokoju.."
        elif text_data_json['header'] == 'MESSAGE':
            answer_msg = f'{player_nickname}: {text_data_json["msg"]}'
        elif text_data_json['header'] == 'START':
            await self.start_game()
            answer_msg = 'game is starting..'

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'answer_msg',
                'msg': answer_msg
            },
        )

    async def answer_msg(self, event):
        msg = event['msg']
        await self.send(json.dumps(msg))

    @database_sync_to_async
    def get_player_nickname(self, player_id):
        return Player.objects.get(id=player_id).nickname

    @database_sync_to_async
    def start_game(self):
        game_room = GameRoom.objects.get(id=self.room_name)
        game_room.is_started = True
        game_room.save()
        