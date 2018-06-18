from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)

class Match(models.Model):
    date = models.DateField()

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date = models.DateField()
    h_goals = models.SmallIntegerField()
    a_goals = models.SmallIntegerField()