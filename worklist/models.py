from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):     # this will provide human readable value on the model
        return self.title

    class Meta:
        ordering = ['complete']   # this will be to retrieve the tasks completed
    
