from django.urls import reverse
from rest_framework.test import APITestCase


class TestExchangeRate(APITestCase):
    def test_exchange_rate_view(self):
        test_cases = [
            ('gbp', '2023-04-21', '5.2086'),
            ('usd', '2023-04-21', '4.2006'),
            ('usd', '2023-04-20', '4.2024'),
        ]
        for currency, date, expected_output in test_cases:
            url = reverse('exchange', kwargs={'currency': currency, 'date': date})
            response = self.client.get(url)
            self.assertEqual(response.data['data']['exchange_rate'], expected_output)


class TestIncorrectCurrencies(APITestCase):
    def test_not_existing_currency(self):
        test_cases = [
            ('123', '2023-04-21', "Wrong details"),
            ('abc', '2023-04-21', "Wrong details"),
            ('usds', '2023-04-21', "Wrong details"),
            ('gbpa', '2023-04-21', "Wrong details"),
            ('gbp', '20231-04-21', "Wrong details"),
            ('gbp', '2021-02-30', "Wrong details"),
            ('1', '1', "Wrong details"),
        ]
        for currency, date, expected_output in test_cases:
            url = reverse('exchange', kwargs={'currency': currency, 'date': date})
            response = self.client.get(url)
            self.assertEqual(response.data['data'], expected_output)


class TestHolidaysAndWeekends(APITestCase):
    def test_selected_date_is_holiday_or_weekend(self):
        test_cases = [
            ('usd', '2023-04-22', 'Wrong details'),
            ('gbp', '2023-04-22', 'Wrong details'),
            ('gbp', '2023-04-23', 'Wrong details'),
            ('gbp', '2023-01-06', 'Wrong details'),
            ('gbp', '2023-04-09', 'Wrong details'),
            ('gbp', '2023-04-10', 'Wrong details'),
            ('usd', '2023-04-10', 'Wrong details'),
            ('aud', '2023-04-10', 'Wrong details'),
        ]
        for currency, date, expected_output in test_cases:
            url = reverse('exchange', kwargs={'currency': currency, 'date': date})
            response = self.client.get(url)
            self.assertEqual(response.data['data'], expected_output)
