from django.test import TestCase
from .models import User
import factory
import random
# Create your tests here.


class RandomUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)
    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_user_model(self):
        self.assertIsInstance(self.user, User)


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_get_user(self):
        resp = self.client.get(f'/users/router/{self.user.id}')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('first_name'), self.user.first_name)

    def test_user_create(self):
        user_data = {
            'first_name': 'Name',
            'last_name': 'Surname',
            'age': 42
        }
        resp = self.client.post('/users/router', data=user_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get('first_name'), user_data.get('first_name'))

    def test_user_delete(self):
        resp = self.client.delete(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)
