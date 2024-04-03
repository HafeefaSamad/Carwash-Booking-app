from django.urls import path
from . import views

urlpatterns = [
    
    path('model/<int:category_id>/', views.VehicleModelView.as_view(), name='model'),
    path('variation/<int:model_id>/', views.VariationView.as_view(), name='variation'),

]