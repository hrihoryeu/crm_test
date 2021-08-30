from django.db import models
from django_countries import fields
from django_extensions.db.fields import AutoSlugField


class Employee(models.Model):
    birth_date = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Company(models.Model):
    title = models.CharField(max_length=30)
    location = fields.CountryField()
    number_of_offices = models.IntegerField()
    number_of_employees = models.IntegerField(blank=True, null=True)
    establishment = models.DateField(auto_created=True)
    cooperation = models.ManyToManyField('self', blank=True)
    is_active = models.BooleanField(default=True)
    employees = models.ManyToManyField(Employee, blank=True, through='Membership')
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from=['employee', 'company'])
    created = models.DateTimeField(auto_now_add=True)
    saved = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
