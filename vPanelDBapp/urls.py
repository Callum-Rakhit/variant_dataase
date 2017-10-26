from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', view=views.home_page, name='home'),
    url(r'^panel/new/$', views.panel_new, name='panel_new'),
    url(r'^$', views.panel_list, name='panel_list'),
    url(r'^panel/(?P<pk>\d+)/$', views.panel_detail, name='panel_detail'),
    url(r'^panel/(?P<pk>\d+)/edit/$', views.panel_edit, name='panel_edit'),
    url(r'^subpanel_new/$', view=views.subpanel_new, name='subpanel_new'),
    url(r'^subpanel/', view=views.subpanel_list, name='subpanel_list'),
    url(r'^subpanel/(?P<pk>\d+)/$', views.subpanel_detail, name='subpanel_detail'),
    url(r'^subpanel/(?P<pk>\d+)/edit/$', views.subpanel_edit, name='subpanel_edit'),
    url(r'^new_hugogene', views.new_hugogene, name='new_hugogene'),
    url(r'^hugogene_list/(?P<pk>\d+)$', views.HUGOListView.as_view(), name='hugogene_list'),
    url(r'^book/(?P<pk>\d+)$', views.HUGODetailView.as_view(), name='hugogene_detail'),
]
