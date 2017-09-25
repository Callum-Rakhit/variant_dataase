from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^newpanel/$', view=views.new_panel, name='NewPanel'),
    url(r'^panellist/$', view=views.panel_list, name='PanelList'),
    url(r'^home/$', view=views.home_page, name='home'),
    url(r'^genes/$', view=views.gene_list, name='genes')
]
