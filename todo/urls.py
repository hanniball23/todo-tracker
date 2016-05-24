from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/impressum/$', views.todo_impressum, name='todo_impressum'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/(?P<pk>\d+)/delete/$', views.todo_delete, name='todo_delete'),
]