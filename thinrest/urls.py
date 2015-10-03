from django.conf.urls import patterns, include, url

from tastypie.api import NamespacedApi

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .api import EmployeeResource, SettingResource

v1_api = NamespacedApi(api_name='v1', urlconf_namespace='')
v1_api.register(EmployeeResource())
v1_api.register(SettingResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'thinrest.views.home', name='home'),
    # url(r'^thinrest/', include('thinrest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
