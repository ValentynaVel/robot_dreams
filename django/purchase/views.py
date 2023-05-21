from django.http import JsonResponse
from .models import Purchase
from django.views.generic import ListView, CreateView, DetailView
from purchase.forms import PurchaseForm


class PurchaseListView(ListView):
    # queryset = User.objects.all()
    model = Purchase


class PurchaseDetailView(DetailView):
    model = Purchase


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = '/purchase/list'




