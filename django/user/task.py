from celery import shared_task
from .models import User
from purchase.models import Purchase


@shared_task
def print_text():
    print('This is some text')


@shared_task(bind=False)
def purchase_count(user_id):
    purchases = Purchase.objects.filter(user_id=user_id).count()
    print(purchases)

    @shared_task
    def user_count():
        users = User.objects.count()
        print(users)
