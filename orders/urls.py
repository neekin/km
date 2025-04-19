from django.urls import path
from .views import OrderCreateAPIView

urlpatterns = [
    path('create/', OrderCreateAPIView.as_view(), name='order-create'),
    # path('health_check/', HealthCheckAPIView.as_view(), name='health-check'),
]