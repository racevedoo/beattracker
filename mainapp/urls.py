from django.conf.urls import patterns, url


urlpatterns = patterns('mainapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^upload/$', 'upload_track', name='upload'),
)



