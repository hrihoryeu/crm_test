from django.shortcuts import render, HttpResponse, get_object_or_404

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin

from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer

# Create your views here.


def first(request):
    return HttpResponse('hello u r gay\nim not but u r')


class CompanyView(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        return self.queryset


class EmployeeView(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return self.queryset
