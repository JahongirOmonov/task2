from django.db import models

# Create your models here.


class fullname(models.Model):
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    thirdname = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.name


class location(models.Model):
    city = models.CharField(max_length=201, default='')
    country = models.CharField(max_length=201, default='')

    def __str__(self) -> str:
        return self.city
