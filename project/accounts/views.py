from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import RegularUser
from accounts.serializers import RegularUserSerializer
from rest_framework import generics

class RegularUserList(generics.ListCreateAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer

class RegularUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

def logout_view(request):
    logout(request)

@login_required
def test_login(request):
    return HttpResponse("User is logged in")

def test_index(request):
    return HttpResponse("Index")
