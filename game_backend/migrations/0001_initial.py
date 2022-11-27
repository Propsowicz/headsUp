# Generated by Django 4.0.6 on 2022-11-27 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GameRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_backend.gameroom')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('game_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_backend.gameroom')),
                ('player', models.ManyToManyField(to='player.player')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('game_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_backend.gameround')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('TAK', 'TAK'), ('NIE', 'NIE')], max_length=3)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_backend.question')),
            ],
        ),
    ]