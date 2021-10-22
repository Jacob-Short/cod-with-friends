from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone




class UserAccount(AbstractUser):
    """
        | Field           | Details              |
        | :-------------- | :------------------  |
        | first_name      | 150 chars            |
        | last_name       | 150 chars            |
        | picture         | ImageField           |
        | display_name    | 150 chars            |
        | date_joined     | def=timezone         |
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images/', max_length=100, default='images/download.png')
    display_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username


