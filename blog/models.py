from email.policy import default
from operator import mod
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title