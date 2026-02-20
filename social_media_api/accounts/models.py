from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=150, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    def __str__(self):
        return self.username