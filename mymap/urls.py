from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'mymap.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'mymap.views.detail', name='detail'),
    url(r'^new/$', 'mymap.views.new', name='new'),
    url(r'^(?P<pk>\d+)/edit/$', 'mymap.views.edit', name='edit'),
    url(r'^(?P<pk>\d+)/comment/new/$', 'mymap.views.comment_new', name='comment_new'),
    url(r'^(?P<pk>\d+)/delete/$', 'mymap.views.delete', name='delete'),
    url(r'^(?P<pk>\d+)/(?P<comment_pk>\d+)/comment/delete/$', 'mymap.views.comment_delete', name='comment_delete'),
]
