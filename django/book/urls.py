from django.urls import path
from . import views
from book.views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    # path('', views.books, name='books'),
    path('list', BookListView.as_view(), name='book-list'),
    path('create', BookCreateView.as_view(), name='book-create'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail')
]
