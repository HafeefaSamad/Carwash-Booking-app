from rest_framework import serializers
from .models import AvailableSlot

class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailableSlot
        fields = '__all__'