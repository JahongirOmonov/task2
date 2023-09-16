from django.shortcuts import render, get_object_or_404
from .models import fullname, location
from django.http import JsonResponse
from .serializer import fullnameSerializer, locationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

class GetAllFullname(generics.ListAPIView):
    queryset=fullname.objects.all()
    serializer_class=fullnameSerializer

class GetDetailFullname(generics.RetrieveAPIView):
    queryset = fullname.objects.all()
    serializer_class=fullnameSerializer

class PostFullname(generics.CreateAPIView):
    queryset=fullname.objects.all()
    serializer_class=fullnameSerializer

class PatchFullname(generics.UpdateAPIView):
    queryset=fullname.objects.all()
    serializer_class=fullnameSerializer

class DeleteFullname(generics.DestroyAPIView):
    queryset=fullname.objects.all()
    serializer_class=fullnameSerializer

class PostGetFullname(generics.ListCreateAPIView):
    queryset=fullname.objects.all()
    serializer_class=fullnameSerializer

class AllFunctionFullname(generics.RetrieveUpdateDestroyAPIView):
    queryset=fullname.objects.all()
    serializer_class=fullnameSerializer

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class GetAllLocation(generics.ListAPIView):
    queryset=location.objects.all()
    serializer_class=locationSerializer

class GetDetailLocation(generics.RetrieveAPIView):
    queryset = location.objects.all()
    serializer_class=locationSerializer

class PostLocation(generics.CreateAPIView):
    queryset=location.objects.all()
    serializer_class=locationSerializer

class PatchLocation(generics.UpdateAPIView):
    queryset=location.objects.all()
    serializer_class=locationSerializer

class DeleteLocation(generics.DestroyAPIView):
    queryset=location.objects.all()
    serializer_class=locationSerializer

class PostGetLocation(generics.ListCreateAPIView):
    queryset=location.objects.all()
    serializer_class=locationSerializer

class AllFunctionLocation(generics.RetrieveUpdateDestroyAPIView):
    queryset=location.objects.all()
    serializer_class=locationSerializer

