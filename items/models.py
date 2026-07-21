from django.db import models

# Create your models here.

class Furniture(models.Model):
    item_name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name