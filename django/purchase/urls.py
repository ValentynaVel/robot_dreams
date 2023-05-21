from django.urls import path
from . import views
from purchase.views import PurchaseListView, PurchaseDetailView, PurchaseCreateView

urlpatterns = [
    # path('', views.purchases, name='purchases'),
    path('list', PurchaseListView.as_view(), name='purchase-list'),
    path('create', PurchaseCreateView.as_view(), name='purchase-create'),
    path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail')
]