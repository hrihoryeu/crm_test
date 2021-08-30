from django.urls import path

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import CompanyView, EmployeeView, MembershipView

router = routers.DefaultRouter()
router.register(r'companies', CompanyView, basename='companies')
router.register(r'employees', EmployeeView, basename='employees')
router.register(r'memberships', MembershipView, basename='memberships')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
