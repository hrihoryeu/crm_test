from django_filters import rest_framework as filters

from .models import Company, Employee, Membership


class CompanyFilter(filters.FilterSet):
    is_active = filters.BooleanFilter()
    number_of_employees = filters.RangeFilter()

    class Meta:
        model = Company
        fields = ['is_active', 'number_of_employees']


class EmployeeFilter(filters.FilterSet):
    is_active = filters.BooleanFilter()
    birth_date = filters.DateFilter()

    class Meta:
        model = Employee
        fields = ['is_active', 'birth_date']


class MembershipFilter(filters.FilterSet):
    position = filters.CharFilter()

    class Meta:
        model = Membership
        fields = ['position']
