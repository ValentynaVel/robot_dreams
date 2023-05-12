from django.db import models
from book.models import Book
from user.models import User


class Purchase(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'purchase'

