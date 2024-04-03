from rest_framework import serializers
from .models import VehicleCategory, VehicleModel, WashType, Variation

class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = VehicleCategory
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleModel
        fields = '__all__'

class WashTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashType
        fields = '__all__'

        
class VariationSerializer(serializers.ModelSerializer):
    wash_type_name = serializers.CharField(source='wash_type.name', read_only=True)

    class Meta:
        model = Variation
        fields = ['id', 'price', 'vehicle_model', 'wash_type', 'wash_type_name']