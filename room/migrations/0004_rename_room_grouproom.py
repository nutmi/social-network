# Generated by Django 4.1.7 on 2023-06-28 15:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("room", "0003_remove_room_guest_guest"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Room",
            new_name="GroupRoom",
        ),
    ]