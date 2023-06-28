from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Guest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
