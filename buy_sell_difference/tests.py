from django.urls import reverse
from rest_framework.test import APITestCase


class TestInputValidation(APITestCase):
    def test_currency_and_quotation_number_is_valid(self):
        test_cases = [
            ('gbp', 'usd', "Wrong details"),
            ('2', 'usd', "Wrong details"),
            ('gbp', '256', "Wrong details"),
            ('usd', '0', "Wrong details"),
        ]
        for currency, quotation_number, expected_output in test_cases:
            url = reverse('difference', kwargs={'currency': currency, 'quotation_number': quotation_number})
            response = self.client.get(url)
            self.assertEqual(response.data['data'], expected_output)
