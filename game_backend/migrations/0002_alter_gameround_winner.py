# Generated by Django 4.0.6 on 2022-11-27 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('game_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameround',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='player.player'),
        ),
    ]