from rest_framework import serializers
from .models import VehicleClass, VehicleInfo, VehicleOffice, VehicleInfoFull

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleClass
        fields = ('id', 'class_type','daily_rate','extra_rate')

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleOffice
        fields = ('id', 'street','city','state','zipcode','phone')

class VehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VehicleInfo
        fields = ('id', 'make','model','make_year','VIN','LPN','vehicle_class','office_info')

class VehicleFullSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VehicleInfoFull
        fields = ('id', 'make','model','make_year','VIN','LPN','vehicle_class','office_info','class_type','daily_rate','extra_rate')