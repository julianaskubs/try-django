from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), # qndo abrimos a url, somos direcionados pra essa pagina
]
