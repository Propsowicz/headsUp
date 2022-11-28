from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json

class HomePageLobby(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):  
        data = ['pokoj 1', 'pokoj 2', 'pokoj 3']
        await self.accept()
        await self.send(json.dumps(data))


    async def disconnect(self):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        lista = ['1', '2', '3']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'avaible_chats',
                'message': lista
            },
        )

    async def avaible_chats(self, event):
        message = event['message']
        # new_data = await self.create_chat(message)
        await self.send(text_data=json.dumps({
            'message': message,
        }))