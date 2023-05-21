from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from django.views.generic import ListView, CreateView, DetailView
from user.forms import UserForm
from rest_framework.viewsets import ModelViewSet


class UserListView(ListView):
    # queryset = User.objects.all()
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = '/user/list'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



