import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from average_value.serializer import MaxAndMinAverageValueSerializer


class MaxAndMinAverageValue(APIView):
    def get(self, request, currency, quotation_number):
        url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last/{quotation_number}/?format=json'
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"data": "Wrong details"})
        data = response.json()
        currency = data['code']
        values = []
        for line in data['rates']:
            values.append(line['mid'])
        minimal_value = min(values)
        maximal_value = max(values)
        data = {"currency": currency, "number_of_quotations": quotation_number,
                'min_value': minimal_value, 'max_value': maximal_value}
        serializer = MaxAndMinAverageValueSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
