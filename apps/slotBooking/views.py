from rest_framework.response import Response 
from rest_framework.views import APIView
from .models import AvailableSlot
from .serializers import SlotSerializer
from rest_framework.permissions import AllowAny
from datetime import datetime, timedelta
# Create your views here.

class AvailableSlotsView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        current_date = datetime.now().date()
        end_date = current_date + timedelta(days=6)
        slots = AvailableSlot.objects.filter(curr_date__range=[current_date, end_date])
        serializer = SlotSerializer(slots, many=True)
        return Response(serializer.data)
    

# class AvailableTimeView(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request):
#             current_date = datetime.now().date()
#             end_date = current_date + timedelta(days=6)
#             slots = AvailableSlot.objects.filter(curr_date__range=[current_date, end_date], is_booked=True)
#             serializer = SlotSerializer(slots, many=True)
#             return Response(serializer.data)
    
class AvailableTimeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        available_slots = AvailableSlot.objects.filter(is_booked=False)

        serialized_slots = [
            {
                "id": slot.id,
                "curr_date": slot.curr_date,
                "start_time": slot.start_time,
                "end_time": slot.end_time,
                "variation": slot.variation.id,
            }
            for slot in available_slots
        ]

        return Response(serialized_slots)