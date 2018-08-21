from django.conf.urls import url

from . import views

app_name = 'iframe'
urlpatterns = [
    url(r'^$', views.iframe, name='iframe'),
]
