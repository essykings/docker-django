from django.db import models
import datetime
import uuid
from django.utils import timezone

now = timezone.now


# Create your models here.


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(default=now)
   
    class Meta:
        app_label = 'tasks'
