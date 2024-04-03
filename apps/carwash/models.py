from django.db import models

# Create your models here.

class VehicleCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class VehicleModel(models.Model):
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.name} - {self.name}"
    
class WashType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Variation(models.Model):
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    wash_type = models.ForeignKey(WashType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.vehicle_model} : Rs:{self.price}"
    
    
    