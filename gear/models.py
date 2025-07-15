from django.db import models
from django.conf import settings


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gear = models.ForeignKey('Gear', on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    trek_date = models.DateField()
    trek_name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def subtotal(self):
        return self.gear.price * self.quantity

class Gear(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='gear_images/')
    available_sizes = models.TextField(blank=True, help_text="Comma-separated sizes")
    
    def __str__(self):
        return self.name

class GearBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    trek_name = models.CharField(max_length=100)
    trek_date = models.DateField()
    size = models.CharField(max_length=50, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.gear.name}"


