from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='kg')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name