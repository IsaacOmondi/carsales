from django.conf.urls import include,url
from .views import *

urlpatterns = [
    url(r'^customer/$', CustomerAPIView.as_view(), name='customer'),
    url(r'^agent/$', AgentAPIView.as_view(), name='agent'),
    url(r'^vehicle/$', VehicleAPIView.as_view(), name='vehicle'),
    url(r'^sale/$', SaleAPIView.as_view(), name='sales'),
]
