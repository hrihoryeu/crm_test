from django.shortcuts import render, HttpResponse, get_object_or_404

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, Employee, Membership
from .serializers import CompanySerializer, EmployeeSerializer, MembershipSerializer
from .permissions import IsAdminOrViewOnly
from .services import CompanyFilter, MembershipFilter, EmployeeFilter


class CompanyView(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter

    permission_classes = (IsAdminOrViewOnly,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        return self.queryset


class EmployeeView(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter

    permission_classes = (IsAdminOrViewOnly,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return self.queryset


class MembershipView(ListModelMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MembershipFilter

    permission_classes = (IsAdminOrViewOnly,)
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def get_queryset(self):
        return self.queryset
