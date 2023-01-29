from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsStaffOrReadOnly

from .models import Company, City, Service
from .serializers import CompanySerializer, ServiceSerializer, CitySerializer


# Create your views here.


class CompanyAPIView(generics.ListAPIView):
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description', "service__name")
    filterset_fields = ('city', )
    ordering_fields = ('name', "service__price")

    def get_queryset(self):
        queryset = Company.objects.prefetch_related("city").prefetch_related("service").all()
        return queryset


class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Company.objects.prefetch_related("city").all()


class CityAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class ServiceAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.select_related("company").all()
