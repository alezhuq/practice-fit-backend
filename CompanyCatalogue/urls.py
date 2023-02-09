from django.urls import path
from .views import CompanyAPIView, CompanyRetrieveUpdateDestroyAPIView, CityAPIView, ServiceAPIView

urlpatterns = [
    path('city/', CityAPIView.as_view()),

    path('service/', ServiceAPIView.as_view()),

    path('company/', CompanyAPIView.as_view()),
    path('company/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view()),
]
