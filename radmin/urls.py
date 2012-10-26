from django.conf.urls import patterns, include, url

urlpatterns = patterns('radmin.views',
    url(r'^ep/$', 'entry_point'),
    url(r'^rnr/$', 'runner'),
)
