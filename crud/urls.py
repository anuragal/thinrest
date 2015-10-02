from django.conf.urls import patterns, include, url

from tastypie.api import NamespacedApi
from .api import EmployeeResource, SettingResource

v1_api = NamespacedApi(api_name='v1', urlconf_namespace='crud')
v1_api.register(EmployeeResource())
v1_api.register(SettingResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
)