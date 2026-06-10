from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class book_list(ListView):
    model=Book
    template_name='list.html'
    context_object_name='emp'
    
class book_detail(DetailView):
    model=Book
    template_name='detail.html'
    
class book_create(CreateView):
    model=Book
    template_name='form.html'
    fields='__all__'
    success_url=reverse_lazy('list')
    
class book_update(UpdateView):
    model=Book
    template_name='form.html'
    fields='__all__'
    success_url=reverse_lazy('list')
    
class book_delete(DeleteView):
    model=Book
    template_name='delete.html'
    success_url=reverse_lazy('list')