from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class Fact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=120,default="")
    fact = models.TextField()

    def __str__(self):
        return self.topic
