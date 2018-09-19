from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def post(self,request, format=None):
    #     first_name = request.data['first_name'],
    #     last_name = request.data['last_name'],
    #     phone_number = request.data['phone_number'],
    #     notes = request.data['notes'] 
    #     user = User.objects.create(
    #         first_name = first_name,
    #         last_name = last_name,
    #         phone_number = phone_number,
    #         notes = notes
    #     )
    #     # user.save()
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


    
        




