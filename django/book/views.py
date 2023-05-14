from django.http import JsonResponse
from .models import Book


def books(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        book_dict = {
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'price': book.price,
        }
        book_list.append(book_dict)
    return JsonResponse({'books': book_list})

