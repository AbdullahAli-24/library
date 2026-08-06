from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    )
    user = models.OneToOneField(  User, on_delete=models.CASCADE )
    role = models.CharField( max_length=20, choices=ROLE_CHOICES, default='member' )
    phone = models.CharField( max_length=15, blank=True)

    def __str__(self):
        return self.user.username