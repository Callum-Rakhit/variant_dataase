from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home/$', view=views.home_page, name='home'),
    url(r'^panel/new/$', views.panel_new, name='panel_new'),
    url(r'^$', views.panel_list, name='panel_list'),
    url(r'^panel/(?P<pk>\d+)/$', views.panel_detail, name='panel_detail'),
    url(r'^panel/(?P<pk>\d+)/edit/$', views.panel_edit, name='panel_edit'),
    url(r'^gene_new/$', view=views.gene_new, name='gene_new'),
    url(r'^gene/', view=views.gene_list, name='gene_list'),
    url(r'^gene/(?P<pk>\d+)/$', views.gene_detail, name='gene_detail'),
    url(r'^gene/(?P<pk>\d+)/edit/$', views.gene_edit, name='gene_edit'),
    url(r'^new_hugogene', views.new_hugogene, name='new_hugogene'),
    url(r'^hugogene_list/(?P<pk>\d+)$', views.HUGOListView.as_view(), name='hugogene_list'),
]
