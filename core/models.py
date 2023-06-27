from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class FriendList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.OneToOneField(User, on_delete=models.CASCADE, related_name="friend")