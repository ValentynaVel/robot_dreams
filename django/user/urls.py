from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from .views import UserListView, UserDetailView, UserCreateView, UserViewSet

urlpatterns = [
    # path('', views.users, name='users'),
    path('list', UserListView.as_view(), name='user-list'),
    path('create', UserCreateView.as_view(), name='user-create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='user-detail')
]

router = SimpleRouter()
router.register('router', UserViewSet)


urlpatterns += router.urls



