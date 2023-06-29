# Generated by Django 4.1.7 on 2023-06-29 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("room", "0005_normalroom"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Message",
            new_name="MessageNormalRoom",
        ),
        migrations.AlterField(
            model_name="messagenormalroom",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="room.normalroom"
            ),
        ),
    ]