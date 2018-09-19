from django.conf.urls import include,url
from .views import *

urlpatterns = [
    url(r'^users/$', UserAPIView.as_view(), name='accounts' ),
    # url(r'^sales/', include('sales.urls', namespace='sales')),
]
from django.conf.urls import include,url
from .views import *

urlpatterns = [
    url(r'^users/$', UserAPIView.as_view(), name='accounts' ),
]
