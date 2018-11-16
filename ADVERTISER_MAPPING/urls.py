from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', views.getapi, name='getapi'),
    url(r'^attendance/$', views.current_datetime, name='today'),
    url(r'^mobidiscover/$', views.mobidiscover, name='Attandance'),
    url(r'^realtimediff/$', views.show_realtime_time_diff, name='reatimediff')



];
