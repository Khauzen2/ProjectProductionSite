# VIEWS

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServiceSerializer

class ServiceList(APIView):
    def get(self, request):
        services = [
            {"name" : "Website Development", "description" : "Custom website tailored to your needs."},
            {"name" : "App Development", "description" : "Mobile and web applications."},
            {"name" : "System Development", "description" : "Complex software solutions."},
        ]
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


