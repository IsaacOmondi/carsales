from django.conf.urls import include,url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Carsales API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^sales/', include('sales.urls', namespace='sales')),
    url(r'^docs/', schema_view),
]
