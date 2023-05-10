from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchases, name='purchases'),
]

