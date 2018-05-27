from rest_framework import serializers
from accounts.models import RegularUser

class RegularUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUser
        password = serializers.CharField(
            style={'input_type': 'password'}
        )
        fields = ('id', 'password', 'email', 'gender', 'birthday', 'confirmed', 'active', 'staff')

    def create(self, validated_data):
        user = RegularUser(
            email=validated_data['email'],
            gender=validated_data['gender'],
            birthday=validated_data['birthday'],
            confirmed=validated_data['confirmed'],
            active=validated_data['active'],
            staff=validated_data['staff'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
