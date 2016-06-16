# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'lists'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^newlist/$', views.create_list, name='newlist'),
    url(r'^details/(?P<type>[A-Z]{1}[a-z]+)/(?P<ran1>[0-9]+)/(?P<ran2>[0-9]+)$',views.item_view,name='details'),
]
