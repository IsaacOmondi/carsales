from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics

# Create your views here.
class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AgentAPIView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class VehicleAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class SaleAPIView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CustomerDetailAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerDetailSerializer