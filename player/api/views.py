from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from player.models import Player
from .serializers import PlayerSerializer

class CreateUserAPI(APIView):
    def post(self, request):
        data = request.data        
        if data['sex'] == 'female':
            new_user = Player.objects.create(nickname='Justyna')
        else:
            new_user = Player.objects.create(nickname='Tomasz')
        serializer = PlayerSerializer(new_user, many=False)
        return Response(serializer.data)
    
