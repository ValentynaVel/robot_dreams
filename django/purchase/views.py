from django.http import JsonResponse
from .models import Purchase
from .serializers import PurchaseSerializer
from django.views.generic import ListView, CreateView, DetailView
from purchase.forms import PurchaseForm
from rest_framework.viewsets import ModelViewSet


class PurchaseListView(ListView):
    # queryset = User.objects.all()
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchase/list'


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer






