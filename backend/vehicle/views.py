from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VehicleSerializer
from django.http import HttpResponse
from .models import VehicleInfo



class VehicleView(APIView):
    def get(self, request):
        vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE city = \'Chicago\' AND rented =0;') 
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    # get(self, request):
    #    vehicles =VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE rented =0;')
    #    serializer = VehicleSerializer(vehicles, many=True)
    #    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

#class VehicleDetailView(APIView):
#    def get(self, request):
#        vehicles = VehicleInfo.objects.raw('SELECT * FROM vehicle_vehicleinfo JOIN vehicle_vehicleoffice ON vehicle_vehicleinfo.office_info_id = vehicle_vehicleoffice.id WHERE city = \'Chicago\' AND rented =0;') 
#        serializer = VehicleSerializer(vehicles, many=True)
#        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    

        