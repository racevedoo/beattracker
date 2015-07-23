from django.conf.urls import patterns, url


urlpatterns = patterns('mainapp.views',
    url(r'^index/(\d+)/(\d+)/$', 'index', name='index'),
    url(r'^index/$', 'index', name='index'),
)



