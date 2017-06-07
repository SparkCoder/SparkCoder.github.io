from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='homeb'),
    url(r'^post/$', views.post, name='postb'),
    url(r'^(?P<postn>[0-9]+)/$', views.details, name='detailsb'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.edit_post, name='editb'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.delete_post, name='deleteb'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.add_comment, name='commentb'),
]
