from django.shortcuts import render
from .models import Books
from .forms import BookForm
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy

class BookList(ListView):
    model = Books
    template_name = 'book/booklist.html'

class BookCreate(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book/bookcreate.html'
    success_url = reverse_lazy('booklist')

class BookUpdate(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book/bookupdate.html'
    success_url = reverse_lazy('booklist')

class BookDetail(DetailView):
    model = Books
    template_name = 'book/bookdetail.html'

class Bookdelete(DeleteView):
    model = Books
    template_name = 'book/bookdelete.html'
    success_url = reverse_lazy('booklist')


