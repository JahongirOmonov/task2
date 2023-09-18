from rest_framework import serializers
from .models import fullname, location
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class fullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model=fullname
        fields=('name','surname','thirdname', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(fullnameSerializer, self).create(validated_data)

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model=location
        fields=('city', 'country', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(locationSerializer, self).create(validated_data)