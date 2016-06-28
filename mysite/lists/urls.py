# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'lists'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^newlist/(?P<item_id>[0-9]+)$', views.create_and_add, name='newlist'),
    url(r'^newlist/$', views.create_list, name='newlist'),
    url(r'^add/(?P<list_id>[0-9]+)/(?P<item_id>[0-9]+)$', views.add_item, name='add'),
    url(r'^remove_item/(?P<list_id>[0-9]+)/(?P<item_id>[0-9]+)$', views.remove_item, name='remove_item'),
    url(r'^details/(?P<type>[A-Z]{1}[a-z]+)/(?P<ran1>[0-9]+)/(?P<ran2>[0-9]+)$',views.item_view,name='details'),
    url(r'^detail/(?P<list_id>[0-9]+)$', views.list_view, name='detail'),
    url(r'^visibility/(?P<list_id>[0-9]+)$', views.visibility, name='visibility'),
    url(r'^delete/(?P<list_id>[0-9]+)$', views.delete, name='delete'),
    url(r'^edit_list/(?P<list_id>[0-9]+)$', views.edit_list, name='edit_list'),
]
