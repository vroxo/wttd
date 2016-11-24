from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Vitor',
            cpf='12345678901',
            email='vitor@mail.com',
            phone='21-981275014'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Vitor', str(self.obj))

    def test_paid_defaul(self):
        self.assertEqual(False, self.obj.paid)

