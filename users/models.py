from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STATUS = (
        ('general', 'GENERAL'),
        ('premium', 'PREMIUM'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars')
    study = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=STATUS, default='general')
    about = models.TextField()
    skills = models.CharField(max_length=250)
    experience = models.TextField()
    interest = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    case = models.CharField(max_length=250)
    groups = models.CharField(max_length=250)
    chat = models.CharField(max_length=250)
    target = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
