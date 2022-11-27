from django.test import TestCase
from .models import Score, GameRoom, GameRound, Question, Answer
from player.models import Player, GenericAvatar

class WorkOfApp(TestCase):
    def setUp(self):
        self.avatar = GenericAvatar.objects.create()
        self.p1 = Player.objects.create(nickname='spiderman', avatar=self.avatar)
        self.p2 = Player.objects.create(nickname='hulk', avatar=self.avatar)
        self.p3 = Player.objects.create(nickname='thor', avatar=self.avatar)
        self.p4 = Player.objects.create(nickname='ironman', avatar=self.avatar)

        self.game_room = GameRoom.objects.create()

    def test_question(self):
        game_round = GameRound.objects.create(game_room=self.game_room)
        question = Question.objects.create(game_round=game_round, player=self.p1, question='Is the sun yellow?')
        Answer.objects.create(question=question, player=self.p2, answer='TAK')
        Answer.objects.create(question=question, player=self.p3, answer='TAK')
        Answer.objects.create(question=question, player=self.p4, answer='NIE')
        qty_of_YES = Answer.objects.filter(answer='TAK').count()

        self.assertEqual(qty_of_YES, 2)


    