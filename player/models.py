from django.db import models


class GenericAvatar(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

class Player(models.Model):
    nickname = models.CharField(max_length=155)
    avatar = models.ForeignKey(GenericAvatar, on_delete=models.SET_NULL, null=True, blank=True)