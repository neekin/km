from django.urls import path
from .views import LicenceCreateAPIView,HealthCheckAPIView

urlpatterns = [
    path('create/', LicenceCreateAPIView.as_view(), name='licence-create'),
    path('health_check/', HealthCheckAPIView.as_view(), name='health-check'),
]