# -*-coding:utf-8-*-

from django.db import models
from django.contrib.auth.models import User


class Reader(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=16, unique=True)
    phone = models.IntegerField(unique=True)
    max_borrowing = models.IntegerField(default=5)
    balance = models.FloatField(default=0.0)
    photo = models.ImageField(blank=True, upload_to='images/')

    STATUS_CHOICES = (
        (0, 'normal'),
        (-1, 'overdue')
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
    )

    def __str__(self):
        return self.name

