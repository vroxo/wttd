from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Vitor Roxo", cpf="13830124740", email="vitor.icnv@gmail.com", phone="21-98127-5014")
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'vitor.icnv@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_to(self):

        contents = [
            'Vitor Roxo',
            '13830124740',
            'vitor.icnv@gmail.com',
            '21-98127-5014'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
