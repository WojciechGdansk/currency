from rest_framework import serializers


class ExchangeRateSerializer(serializers.Serializer):
    currency = serializers.CharField()
    date = serializers.CharField()
    exchange_rate = serializers.CharField()

    def to_representation(self, instance):
        return {"data": instance}

