from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),  # qndo abrimos a url, somos direcionados pra essa pagina
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]
