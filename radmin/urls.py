try:
    # django 1.4
    from django.conf.urls import *
    urlpatterns = patterns('radmin.views',
        url(r'^ep/$', 'entry_point'),
        url(r'^rnr/$', 'runner'),
    )
except NameError:
    # django 1.3.4
    from django.conf.urls.defaults import patterns, url

    urlpatterns = patterns('radmin.views',
        url(r'^ep/$', 'entry_point'),
        url(r'^rnr/$', 'runner'),
    )
