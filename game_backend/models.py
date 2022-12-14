from django.db import models
from player.models import Player, GenericAvatar

class GameRoom(models.Model):
    player = models.ManyToManyField(Player)
    is_started = models.BooleanField(default=False)
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'

# class Score(models.Model):
#     game_room = models.ForeignKey(GameRoom, on_delete=models.CASCADE)
#     player = models.ManyToManyField(Player)
#     score = models.IntegerField()

#     def __str__(self):
#         return f'{self.game_room} || {self.player} || {self.score}'

class GameRound(models.Model):
    game_room = models.ForeignKey(GameRoom, on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'The winner of round {self.id} is {self.winner}.'

class Question(models.Model):
    game_round = models.ForeignKey(GameRound, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.game_round} || {self.player} || {self.question}'

class Answer(models.Model):
    case = [
        ('TAK','TAK'),
        ('NIE', 'NIE'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    answer = models.CharField(max_length=3, choices=case)

    def __str__(self):
        return f'{self.question} || {self.player} || {self.answer}'

class GuessCharacter(models.Model):
    name = models.CharField(max_length=155)

    def __start__(self):
        return self.name