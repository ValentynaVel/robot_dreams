from django.db import models
from book.models import Book
from user.models import User


class Purchase(models.Model):
    date = models.DateField()
    user = models.ManyToManyField(User, related_name="purchase")
    book = models.ManyToManyField(Book, related_name="purchase")

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return f"{self.id}: {self.date} {self.user} {self.book}"

