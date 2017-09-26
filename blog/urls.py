from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.panel_list, name='panel_list'),
    url(r'^panel/(?P<pk>\d+)/$', views.panel_detail, name='panel_detail'),
    url(r'^panel/new/$', views.panel_new, name='panel_new'),
    url(r'^panel/(?P<pk>\d+)/edit/$', views.panel_edit, name='panel_edit'),
    url(r'^home/$', view=views.home_page, name='home'),
    url(r'^genes/$', view=views.gene_list, name='genes')
]
