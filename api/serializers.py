from api.models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model=User
        fields=["first_name","last_name","email","username","password"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

