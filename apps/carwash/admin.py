from django.contrib import admin
from .models import VehicleCategory, VehicleModel,WashType, Variation
# Register your models here.

admin.site.register(VehicleCategory)
admin.site.register(VehicleModel)
admin.site.register(WashType)
admin.site.register(Variation)