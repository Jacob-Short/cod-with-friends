from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from loadouts.models import Loadout
from accounts.models import UserAccount


class Soldier(models.Model):
    """
        | Field           | Details              |
        | :-------------- | :------------------  |
        | name            | 150 chars            |
        | loadout         | fk loadout           |
        | user_account    | oto user_acc         |
        | picture         | ImageField           |
        | date_joined     | def=timezone         |
    """
    name = models.CharField(max_length=50)
    loadout = models.ForeignKey(Loadout, on_delete=models.CASCADE)
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='soldier_user')
    picture = models.ImageField(upload_to='images/', max_length=100, default='images/download.png')
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username
