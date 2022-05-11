from django.urls import path
from .views import VehicleView,VehicleFullView

urlpatterns = [
    path('', VehicleView.as_view()),
    path('<int:vehicle_id>/', VehicleFullView.as_view()),
    #path('<str:city>/', VehicleCityView.as_view()),
    #path('vehicles/<str:city>/',VehicleView.as_view()),
]