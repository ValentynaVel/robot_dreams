from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(null=False)
    price = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"{self.id}: {self.title} {self.author} {self.year} {self.price}"



