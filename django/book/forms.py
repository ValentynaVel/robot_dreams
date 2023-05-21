from django.forms import *
from .models import Book


class BookForm(ModelForm):
    title = CharField(max_length=200)
    author = CharField(max_length=200)

    class Meta:
        model = Book
        fields = '__all__'
