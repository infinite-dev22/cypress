from datetime import datetime

from django.db import models

from accounts.models import BaseUser


# Create your models here.
class ChatMessages(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name="msg_sender"
    )
    msg_receiver = models.ForeignKey(
        BaseUser,
        on_delete=models.CASCADE,
        related_name="msg_receiver"
    )
    seen = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=datetime.now().astimezone)

    def __str__(self):
        return f"{self.body}"
