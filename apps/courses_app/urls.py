from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^course/add$', views.add),
    url(r'^course/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^comment$', views.comment)
]
