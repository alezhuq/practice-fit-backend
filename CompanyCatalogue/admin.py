from .models import Company, Service, City
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

admin.site.unregister(Group)
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(City)
