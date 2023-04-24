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
            url = reverse('min_and_max_value', kwargs={'currency': currency, 'quotation_number': quotation_number})
            response = self.client.get(url)
            self.assertEqual(response.data['data'], expected_output)


class TestMaxAndMinAverageValue(APITestCase):
    def test_minimal_and_maximal_value(self):
        test_cases = [
            ('gbp', '5', 5.2086, 5.2529),
            ('usd', '255', 4.1905, 5.0381),
            ('aud', '20', 2.8024, 2.8933),
            ('thb', '50', 0.1218, 0.1323),
        ]
        for currency, quotation_number, minimal_value, maximal_value in test_cases:
            url = reverse('min_and_max_value', kwargs={'currency': currency, 'quotation_number': quotation_number})
            response = self.client.get(url)
            self.assertEqual(response.data['data']['min_value'], minimal_value)
            self.assertEqual(response.data['data']['max_value'], maximal_value)
