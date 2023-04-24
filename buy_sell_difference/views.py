import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from buy_sell_difference.serializer import MajorDifferenceSerializer


class MajorDifferenceBetweenButAndSellRate(APIView):
    def get(self, request, currency, quotation_number):
        url = f'https://api.nbp.pl/api/exchangerates/rates/c/{currency}/last/{quotation_number}/?format=json'
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"data": "Wrong details"})
        data = response.json()
        currency = data['code']
        differences = []
        for line in data['rates']:
            differences.append(round(line['ask'] - line['bid'], 4))
        maximal_value = max(differences)
        data = {"currency": currency, "number_of_quotations": quotation_number, 'max_value': maximal_value}
        serializer = MajorDifferenceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
