from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Interest(models.Model):
    name = models.TextField(max_length=240)
    type = models.TextField(max_length=240)

    def __str__(self):
        return self.name


class Profile(models.Model):
    dob = models.DateField(default=False)
    gender = models.TextField(max_length=240)
    name = models.TextField(max_length=240)
    interests = models.ManyToManyField(
        to=Interest,
        symmetrical=False
    )

class Member(User):
    username = models.TextField(max_length=240)
    password = models.TextField(max_length=240)
    profile = models.OneToOneField(
        to=Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

