from django.db import models
from django_countries import fields


class Company(models.Model):
    title = models.CharField(max_length=30)
    location = fields.CountryField()
    number_of_offices = models.IntegerField()
    number_of_employees = models.IntegerField()
    establishment = models.DateField(auto_created=True)
    cooperation = models.ManyToManyField('self', blank=True)
    employee = models.ManyToManyField('Employee', blank=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    birth_date = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
