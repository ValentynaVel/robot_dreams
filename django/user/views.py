from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from django.views.generic import ListView, CreateView, DetailView
from .forms import UserForm
from rest_framework.viewsets import ModelViewSet
from rest_framework.paginator import PageNumberPaginator
from rest_framework import filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['contains'],
            'age': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class CustomPaginator(PageNumberPaginator):
    page_size_query_param = 'page_size'


class UserListView(ListView):
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

    filterset_class = UserFilter

    search_fields = ['first_name', 'last_name', ]
    ordering_fields = ['age', 'id']
    pagination_class = CustomPaginator


    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SeachFilter,
        filters.OderingFilter,
    ]


