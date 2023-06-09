from django.db import models
from django.urls import reverse
from django.db.models import Case, IntegerField, Value, When

class Color(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:color_detail", args=[str(self.id)])


class Transmission(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Engine(models.Model):
    name = models.CharField(max_length=200)
    power = models.CharField(max_length=200)
    type_engine = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}, {self.type_engine} ({self.power} hp.)"

    def get_absolute_url(self):
        return reverse("shop:engine_detail", args=[str(self.id)])

    def get_power_range(self):
        return self.power

    class Meta:
        ordering = ['name']


class ManufacturerCountry(models.Model):
    engine = models.OneToOneField("Engine", on_delete=models.CASCADE)
    country = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.engine.name}, {self.engine.power}"

    def get_absolute_url(self):
        return reverse("shop:manufacturercountry_detail", args=[str(self.id)])


class Car(models.Model):
    model = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    engine = models.ForeignKey("Engine", on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey("Transmission", on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey("Color", on_delete=models.SET_NULL, null=True)
    manufacture_date = models.DateField()

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("shop:car_detail", args=[str(self.id)])


class CarShop(models.Model):
    car = models.ForeignKey("Car", on_delete=models.SET_NULL, null=True)
    count = models.IntegerField()
    receipt_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.model} ({self.count} pcs.)"

    def get_absolute_url(self):
        return reverse("shop:carshop_detail", args=[str(self.id)])


