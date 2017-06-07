from django.conf.urls import url
from polls import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.Index.as_view(), name='indexp'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail.as_view(), name='detailp'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='resultsp'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='votep'),
]
