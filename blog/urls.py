from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<postn>[0-9]+)/$', views.details, name='details'),
]
