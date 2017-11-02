from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.home_page, name='home'),

    url(r'^panel_new/$', views.panel_new, name='panel_new'),
    url(r'^panel/', views.panel_list, name='panel_list'),
    url(r'^panel/(?P<pk>\d+)/$', views.panel_detail, name='panel_detail'),
    url(r'^panel/(?P<pk>\d+)/edit/$', views.panel_edit, name='panel_edit'),

    url(r'^subpanel_new/$', view=views.subpanel_new, name='subpanel_new'),
    url(r'^subpanel/', view=views.subpanel_list, name='subpanel_list'),
    url(r'^subpanel/(?P<pk>\d+)/$', views.subpanel_detail, name='subpanel_detail'),
    url(r'^subpanel/(?P<pk>\d+)/edit/$', views.subpanel_edit, name='subpanel_edit'),

    url(r'^hugogene_new/$', view=views.hugogene_new, name='hugogene_new'),
    url(r'^hugogene/', views.hugogene_list, name='hugogene_list'),
    url(r'^hugogene/(?P<pk>\d+)/$', views.hugogene_detail, name='hugogene_detail'),
    url(r'^hugogene/(?P<pk>\d+)/edit/$', views.hugogene_edit, name='hugogene_edit'),

    url(r'^search_results/$', view=views.search, name='Search'),
]
