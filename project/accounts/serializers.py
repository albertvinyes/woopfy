from rest_framework import serializers
from accounts.models import RegularUser

class RegularUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUser
        fields = ('id', 'email', 'gender', 'birthday', 'confirmed', 'active', 'staff')
