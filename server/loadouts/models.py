from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import manager
from django.db.models.deletion import CASCADE
from accounts.models import UserAccount

from weapons.models import Weapon



class Loadout(models.Model):
    """
        | Field           | Details              |
        | :-------------- | :------------------  |
        | name            | 150 chars            |
        | weapons         | mtm weapon           |
        | picture         | ImageField           |
        | user_account    | fk AccountUser       |
    """
    name = models.CharField(max_length=150)
    weapons = models.ManyToManyField(Weapon, max_length=5)
    picture = models.ImageField(upload_to='images/', max_length=100, default='images/download.png')
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

