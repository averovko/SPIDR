from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='launcher_main')),
    url(r'^main/$', views.main, name='launcher_main'),
]
