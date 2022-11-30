# Generated by Django 4.1.3 on 2022-11-30 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_is_host_player_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuessCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='player.guesscharacter'),
        ),
    ]
