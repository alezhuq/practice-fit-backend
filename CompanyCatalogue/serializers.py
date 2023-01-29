from .models import Company, City, Service

from rest_framework import serializers


class PartialCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name",)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name",)


class PartialServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']


class CompanySerializer(serializers.ModelSerializer):
    city = PartialCitySerializer(many=True, required=False)
    service = PartialServiceSerializer(many=True, required=False)

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'website', 'email', 'phonenum', 'photo', 'city', 'service']
