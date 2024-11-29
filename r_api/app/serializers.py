from rest_framework import serializers
from .models import *

class sample(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    place=serializers.CharField()

class mdl_serializer(serializers.ModelSerializer):
    class Meta:
        model=Api_user
        fields='__all__'