from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    website = models.CharField(max_length=50)
    email = models.EmailField(max_length=20, unique=True)
    phonenum = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank="True")
    city = models.ManyToManyField("City", related_name='city')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='service')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
