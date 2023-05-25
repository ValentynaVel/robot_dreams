from django.urls import path
from . import views
from .views import PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseViewSet
from rest_framework.routers import SimpleRouter


urlpatterns = [
    # path('', views.purchases, name='purchases'),
    path('list', PurchaseListView.as_view(), name='purchase-list'),
    path('create', PurchaseCreateView.as_view(), name='purchase-create'),
    path('detail/<int:pk>', PurchaseDetailView.as_view(), name='purchase-detail')
]


router = SimpleRouter()
router.register('router', PurchaseViewSet)

urlpatterns += router.urls

