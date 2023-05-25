from django.http import JsonResponse
from .models import Book
from django.views.generic import ListView, CreateView, DetailView
from .forms import BookForm
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework import filters


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/book/list'


class BookViewSet(ModelViewSet):
    queryset = Book.object.all()
    serializer_class = BookSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['title', 'author']
    ordering_fields = ['id']





