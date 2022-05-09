from django.urls import path
from .views import VehicleView

urlpatterns = [
    path('vehicles/', VehicleView.as_view()),
    #path('vehicles/<str:city>/',VehicleView.as_view()),
]