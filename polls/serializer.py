from rest_framework import serializers
from .models import fullname, location

class fullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model=fullname
        fields=('name','surname','thirdname')

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model=location
        fields=('city', 'country')