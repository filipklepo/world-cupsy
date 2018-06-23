from django.contrib import admin
from django.contrib.auth.models import User

from .models import Match, UserVote

admin.site.register(User)
admin.site.register(Match)
admin.site.register(UserVote)