from rest_framework import serializers
from .models import Chocolate,Register

# convert our data into json

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chocolate
        fields='__all__'

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields = ['id', 'name', 'phone_number', 'email']


      