from django.contrib import admin
from .models import Booking, AvailableSlot

# Register your models here.
admin.site.register(AvailableSlot)
admin.site.register(Booking)
