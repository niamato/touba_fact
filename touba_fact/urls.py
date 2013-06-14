from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'touba_fact.views.home', name='home'),
    # url(r'^touba_fact/', include('touba_fact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
)

urlpatterns += staticfiles_urlpatterns()
