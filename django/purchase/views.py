from django.http import JsonResponse
from .models import Purchase


def purchases(request):
    purchases = Purchase.objects.all()
    purchase_list = []
    for purchase in purchases:
        purchase_dict = {
            'date': purchase.date,
            'user': purchase.user_id,
            'book': purchase.book_id,
        }
        purchase_list.append(purchase_dict)
    return JsonResponse({'purchases': purchase_list})
