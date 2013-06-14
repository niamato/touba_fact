from django.conf.urls import patterns, url
__author__ = 'nmtsylla'



urlpatterns = patterns('blog.views',
    url(r'^$', 'homepage'),
    url(r'^login/$', 'connexion'),
    url(r'^logout/$', 'deconnexion'),
    url(r'^add_fact/$', 'add'),
    url(r'about/$', 'about'),
    url(r'mouridisme/$', 'mouridisme'),
    url(r'contact/$', 'contact'),
    url(r'fact/(?P<id_fact>\d+)$', 'view_fact'),
    url(r'facts/$', 'list_facts'),
    url(r'facts/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_facts'),

)