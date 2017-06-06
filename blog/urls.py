from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/$', views.post, name='post'),
    url(r'^(?P<postn>[0-9]+)/$', views.details, name='details'),
]
