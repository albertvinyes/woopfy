from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import redirect,render
from accounts.models import RegularUser
from accounts.serializers import RegularUserSerializer
from .auth import AdminOrRegularUserBackend
from rest_framework import generics

class RegularUserList(generics.ListCreateAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer

class RegularUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSerializer

def validateEmail( email ):
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def login_view(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['email']
        password = request.POST['password']
        email_is_valid = validateEmail(username)
        if not email_is_valid:
            return HttpResponse("Invalid email")
        try:
            user = AdminOrRegularUserBackend.authenticate(request, username=username, password=password)
            if user:
                return HttpResponse("User is logged in")
            else:
                return HttpResponse(status=401)
        except:
            return HttpResponse(status=401)
    elif request.method == 'GET':
        return render(request, 'registration/login.html')
    else:
        return HttpResponse(status=405)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def test_login(request):
    return HttpResponse("User is logged in")

def test_index(request):
    return HttpResponse("Index")
