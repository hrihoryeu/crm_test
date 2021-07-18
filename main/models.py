from django.db import models
from django_countries import fields


class Company(models.Model):
    title = models.CharField(max_length=30)
    location = fields.CountryField()
    number_of_offices = models.IntegerField()
    number_of_employees = models.IntegerField()
    establishment = models.DateField(auto_created=True)
    cooperation = models.ManyToManyField('self', blank=True)


class Employee(models.Model):
    birth_date = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.ManyToManyField(Company)
    position = models.JSONField()
