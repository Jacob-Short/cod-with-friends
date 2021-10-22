from django.db import models
from django.db.models.fields import related


class Attachment(models.Model):
    """
    | Field           | Details              |
    | :-------------- | :------------------  |
    | name            | 150 chars            |
    | picture         | ImageField           |
    | details         | textfield            |
    """

    name = models.CharField(max_length=150)
    picture = models.ImageField(
        upload_to="images/", max_length=100, default="images/download.png"
    )
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    """
    | Field           | Details              |
    | :-------------- | :------------------  |
    | name            | 150 chars            |
    | attachments     | mtm attachment       |
    | picture         | ImageField           |
    | details         | textfield            |
    """

    name = models.CharField(max_length=150)
    attachments = models.ManyToManyField(Attachment, related_name="weapon_attachments")
    picture = models.ImageField(
        upload_to="images/", max_length=100, default="images/download.png"
    )
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
