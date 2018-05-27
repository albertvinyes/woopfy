from django.shortcuts import render
from accounts.models import RegularUser
from accounts.serializers import RegularUserSerializer
from rest_framework import generics

class RegularUserList(generics.ListCreateAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer

class RegularUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer
