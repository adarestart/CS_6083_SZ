from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VehicleCitySerializer,VehicleFullSerializer
from django.http import HttpResponse
from .models import VehicleInfo, VehicleOffice



class VehicleView(APIView):
    def get(self, request):
        #print(request.data)
        #vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE rented =0;') 
        #serializer = VehicleSerializer(vehicles, many=True)
        #return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE rented =0;') 
        serializer = VehicleCitySerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
class VehicleFullView(APIView):
    def get(self, request,vehicle_id):
        #vehicle_id = request.query_params.get('id', None)
        if vehicle_id is not None:
            vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleclass ON vehicle_vehicleinfo.vehicle_class_id = vehicle_vehicleclass.id WHERE vehicle_vehicleinfo.id = %s;',[vehicle_id]) 
            serializer = VehicleFullSerializer(vehicles, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            vehicles =[]
            serializer = VehicleFullSerializer(vehicles, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

