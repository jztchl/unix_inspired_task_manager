from django.db import models
from user.models import User
from enum import Enum

class StatusChoices(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20,default=StatusChoices.PENDING.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id}: {self.name} [{self.status}]"
    
