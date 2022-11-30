from django.db import models

class GuessCharacter(models.Model):
    name = models.CharField(max_length=155)

    def __start__(self):
        return self.name

class GenericAvatar(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

class Player(models.Model):
    nickname = models.CharField(max_length=155)
    is_host = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    avatar = models.ForeignKey(GenericAvatar, on_delete=models.SET_NULL, null=True, blank=True)
    character = models.ForeignKey(GuessCharacter, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nickname
    
