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
    success_url = '/books'


# def books(request):
#     books = Book.objects.all()
#     book_list = []
#     for book in books:
#         book_dict = {
#             'title': book.title,
#             'author': book.author,
#             'year': book.year,
#             'price': book.price,
#         }
#         book_list.append(book_dict)
#     return JsonResponse({'books': book_list})

