from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.post_list,name='post_list'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),#view to go to direct posts
url(r'^post/new/$', views.post_new, name='post_new'),#view to making new blopg posts
url('post/new/',views.post_new,name='post_new'),#view to making new blopg posts
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
] 