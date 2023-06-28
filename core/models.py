from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class FriendList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="friend"
    )

    def __str__(self) -> str:
        return f"room of {self.user} with friend {self.friend}"
