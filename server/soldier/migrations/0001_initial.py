# Generated by Django 3.2.7 on 2021-10-22 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loadouts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(default='images/download.png', upload_to='images/')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('loadout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loadouts.loadout')),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='soldier_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
