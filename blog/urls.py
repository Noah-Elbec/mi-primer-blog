from django.urls import include, path, re_path
from . import views

urlpatterns = [
    
    path('',views.post_list, name = 'post_list'),
    re_path('^post/(?P<pk>[0-9]+)/$',views.post_detail,name = 'post_detail'),
    re_path('^post/new/$', views.post_new, name='post_new'),
    re_path('^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]

