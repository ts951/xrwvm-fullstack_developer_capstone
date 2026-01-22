from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    car_types = {
        "SUV": "SUV",
        "COUPE": "Coupe",
        "CONVERTIBLE": "Convertible",
        "MINIVAN": "Minivan",
        "PICK-UP": "Pick-Up",
        "SEDAN": "Sedan"}
    types = models.CharField(max_length=50, choices=car_types, default="SUV")
    validator_ranges = [
            MaxValueValidator(2023),
            MinValueValidator(2015)]
    year = models.IntegerField(default=2023, validators=validator_ranges)

    def __str__(self):
        return self.name
