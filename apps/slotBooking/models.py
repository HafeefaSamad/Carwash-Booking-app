from django.db import models
from apps.carwash.models import Variation
from apps.account.models import CustomUser

# Create your models here.

class AvailableSlot(models.Model):
    curr_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Available Slot - {self.curr_date} - {self.start_time} to {self.end_time}"
    
class Booking(models.Model):
    user = models.ForeignKey( CustomUser, on_delete=models.CASCADE)
    slot = models.ForeignKey(AvailableSlot, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"Booking - {self.user}, Slot: {self.slot}"
     