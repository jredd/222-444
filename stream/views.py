from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic

from . import models


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'four'
    queryset = models.FourVideoStream.objects.all()

    def get_context_data(self, **kwargs):
        """Return the six video list as well"""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['six'] = models.SixVideoStream.objects.order_by('title')
        return context


class FourStreamView(generic.DetailView):
    template_name = 'four_streams.html'
    context_object_name = 'stream'
    queryset = models.FourVideoStream.objects.all()

class SixStreamView(generic.DetailView):
    template_name = 'six_streams.html'
    context_object_name = 'stream'
    queryset = models.SixVideoStream.objects.all()