# Generated by Django 4.1.3 on 2022-11-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_is_host_player_score'),
        ('game_backend', '0002_alter_gameround_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='is_ended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameroom',
            name='is_started',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameroom',
            name='player',
            field=models.ManyToManyField(to='player.player'),
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
