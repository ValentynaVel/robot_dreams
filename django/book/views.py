from django.http import JsonResponse
from .models import Book
from django.views.generic import ListView, CreateView, DetailView
from book.forms import BookForm

class BookListView(ListView):
    # queryset = User.objects.all()
    model = Book


class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/book/list'



