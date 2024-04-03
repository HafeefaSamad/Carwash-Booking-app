from django.urls import path
from . import views

urlpatterns = [
    path('slot/', views.AvailableSlotsView.as_view(), name='slot'),
    path('time/', views.AvailableTimeView.as_view(), name='time'),

   
]
    