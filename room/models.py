from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class GroupRoom(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    amout_of_users = models.IntegerField(default=0)

    def __str__(self) -> str:
        return (f"creator {self.creator}, id {self.id}")


class Guest(models.Model):
    room = models.ForeignKey(GroupRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class NormalRoom(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_2")

    def __str__(self) -> str:
        return (f"room of {self.user_1} and {self.user_2} id {self.id}")
    
class MessageNormalRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    room = models.ForeignKey(NormalRoom, on_delete=models.CASCADE)