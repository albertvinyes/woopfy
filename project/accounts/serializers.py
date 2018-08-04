from rest_framework import serializers
from rest_auth import serializers as authSerializers
from accounts.models import RegularUser
from django.contrib.auth import authenticate

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

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = RegularUser

    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        mail = attrs.get('email')
        password = attrs.get('password')

        user = RegularUser.objects.get(email=mail)
        auth = user.check_password(password)

        print(auth)
        attrs['user'] = user
        return attrs
