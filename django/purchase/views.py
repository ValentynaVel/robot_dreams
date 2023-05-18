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
    success_url = '/purchases'



# def purchases(request):
#     purchases = Purchase.objects.all()
#     purchase_list = []
#     for purchase in purchases:
#         purchase_dict = {
#             'date': purchase.date,
#             'user': purchase.user_id,
#             'book': purchase.book_id,
#         }
#         purchase_list.append(purchase_dict)
#     return JsonResponse({'purchases': purchase_list})
