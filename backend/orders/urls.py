from django.urls import path
from .views import OrderView, InvoiceView,PaymentView
urlpatterns = [
    path('', OrderView.as_view()),
    path('invoice/', InvoiceView.as_view()),
    path('payment/',PaymentView.as_view()),
    #path('vehicles/<int:vehicle_id>/', VehicleFullView.as_view()),
    #path('vehicles/<str:city>/',VehicleView.as_view()),
]