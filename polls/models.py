from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class fullname(models.Model):
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    thirdname = models.CharField(max_length=200, default='')
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name


class location(models.Model):
    city = models.CharField(max_length=201, default='')
    country = models.CharField(max_length=201, default='')
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.city   
