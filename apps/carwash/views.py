from rest_framework.response import Response
from rest_framework.views import APIView
from .models import VehicleCategory, VehicleModel, WashType, Variation
from .serializers import CategorySerializer, ModelSerializer, WashTypeSerializer, VariationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

# class CategoryView(APIView):
#     permission_classes = (AllowAny,)
#     def get(self, request):
#         categories = VehicleCategory.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response (serializer.data)

class VehicleModelView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, category_id):
        model = VehicleModel.objects.filter(category_id = category_id)
        serializer = ModelSerializer(model, many=True)
        return Response(serializer.data)

class VariationView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, model_id):
        wash_type = Variation.objects.filter(vehicle_model_id=model_id)
        serializer = VariationSerializer(wash_type, many=True)
        return Response(serializer.data)
        
