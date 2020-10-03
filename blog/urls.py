from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^all/', views.post_list, name='post_list'),
    url(r'^blogs/(?P<slug>[\w\-]+)/', views.post_detail, name='post_detail'),
    # url(r'^blogs/$', views.post_detail, name='post_detail'),
    url(r'^tag/(?P<slug>[\w\-]+)/', views.post_list, name='post_list_by_tag'),

]
