from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    group = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    date = models.DateField()
    h_goals = models.SmallIntegerField()
    a_goals = models.SmallIntegerField()
    finished = models.BooleanField()

    def __str__(self):
        return '{date} {title} ({gr}) {hg}:{ag} {fin}'.format(
            date=self.date, title=self.title, gr=self.group, hg=self.h_goals,
            ag=self.a_goals, fin=('' if self.finished else 'NOT ') + 'FINISHED')

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    h_goals = models.SmallIntegerField()
    a_goals = models.SmallIntegerField()

    def __str__(self):
        return '{user}: {match}: {date}: {h_goals}:{a_goals}'.format(
            user=self.user,
            match=self.match,
            date=self.date,
            h_goals=self.h_goals,
            a_goals=self.a_goals)