from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Trek(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='treks')
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    best_month = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    trek = models.ForeignKey(Trek, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} – {self.trek} ({self.rating}★)"

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    email = models.EmailField(unique=True)





