from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from django.views.generic import ListView, CreateView, DetailView
from user.forms import UserForm


class UserListView(ListView):
    # queryset = User.objects.all()
    model = User


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = '/users'

#
# def users(request):
#     users = User.objects.all()
#     user_list = []
#     for user in users:
#         user_dict = {
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'age': user.age
#         }
#         user_list.append(user_dict)
#     return JsonResponse({'users': user_list})
#


