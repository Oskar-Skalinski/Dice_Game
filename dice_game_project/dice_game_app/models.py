from django.db import models

class Game(models.Model):
    player = models.CharField(max_length=50)
    points = models.IntegerField()
    rolls = models.IntegerField()