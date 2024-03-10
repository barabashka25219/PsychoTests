from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(
        choices = (
            ('M', 'Male'),
            ('F', 'Female'),
        ),
        max_length=1,
        blank=True
    )
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=800, blank=True)