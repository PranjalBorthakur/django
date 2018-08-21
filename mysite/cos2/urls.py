from django.conf.urls import url

from . import views

app_name = 'cos2'
urlpatterns = [
    url(r'^$', views.cos2, name='cos2'),
]
