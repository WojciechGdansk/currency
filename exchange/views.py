import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from exchange.serializer import ExchangeRateSerializer


class Exchange(APIView):
    def get(self, request, currency, date):
        response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json')
        if response.status_code != 200:
            return Response({"data": "Wrong details"})
        data = response.json()
        currency = data['code']
        exchange_rate = data['rates'][0]['mid']
        data = {'currency': currency, "date": date, 'exchange_rate': exchange_rate}
        serializer = ExchangeRateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
