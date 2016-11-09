from django.conf.urls import url

from . import views

urlpatterns = [
    url('two/(?P<pk>[a-z-A-Z-0-9]+)/$', views.TwoStreamView.as_view()),
    url('four/(?P<pk>[a-z-A-Z-0-9]+)/$', views.FourStreamView.as_view()),
    url('six/(?P<pk>[a-z-A-Z-0-9]+)/$', views.SixStreamView.as_view()),
]