from rest_framework import serializers


class MaxAndMinAverageValueSerializer(serializers.Serializer):
    currency = serializers.CharField()
    number_of_quotations = serializers.IntegerField()
    min_value = serializers.FloatField()
    max_value = serializers.FloatField()

    def to_representation(self, instance):
        return {"data": instance}
