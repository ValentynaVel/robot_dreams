from django.db import models
from django.book.models import Book
from django.user.models import User


class Purchase(models.Model):
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'purchase'

