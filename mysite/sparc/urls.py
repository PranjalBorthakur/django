from django.conf.urls import url

from . import views

app_name = 'sparc'
urlpatterns = [
    url(r'^$', views.sparc, name='sparc'),
    url(r'^polls1/$', views.polls1, name='polls1'),
    url(r'^iconnect/$', views.iconnect, name='iconnect'),

]

