from django.conf.urls import url

from . import views

urlpatterns = [
    url('four/(?P<pk>[a-z-A-Z-0-9]+)/$', views.FourStreamView.as_view()),
    url('six/(?P<pk>[a-z-A-Z-0-9]+)/$', views.SixStreamView.as_view()),
]