from rest_framework import serializers
from .models import *


class UserRegisterSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'username', 'is_staff', 'password')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        fields = '__all__'