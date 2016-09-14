from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='launcher_main'), name='launcher_home'),
    url(r'^main/$', views.main, name='launcher_main'),
    url(r'^(?P<app_name>[^/]+)/$', views.launch_app, name='launch_app'),
    url(r'^(?P<app_name>[^/]+)/(?P<dashboard_name>[^/]+)/$', views.launch_app_dashboard, name='launch_app_dashboard'),
]
