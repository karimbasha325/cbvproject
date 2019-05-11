from django.shortcuts import render
from testapp.models import Mobile
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class Mobilelistview(ListView):
    model=Mobile

class Mobiledetailview(DetailView):
    model=Mobile

class Mobilecreateview(CreateView):
    model=Mobile
    fields='__all__'

class Mobileupdateview(UpdateView):
    model=Mobile
    fields=('ram','camera','price')
    #success_url=reverse_lazy('detail')

class Mobiledeleteview(DeleteView):
    model=Mobile
    success_url=reverse_lazy('list')
