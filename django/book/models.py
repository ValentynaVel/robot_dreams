from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(null=False)
    price = models.PositiveSmallIntegerField(null=False)

    class Meta:
        db_table = 'book'



