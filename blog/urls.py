from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/$', views.post, name='post'),
    url(r'^(?P<postn>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.edit_post, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.delete_post, name='delete'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.add_comment, name='comment'),
]
