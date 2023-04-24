from rest_framework import serializers


class MajorDifferenceSerializer(serializers.Serializer):
    currency = serializers.CharField()
    number_of_quotations = serializers.IntegerField()
    max_value = serializers.FloatField()

    def to_representation(self, instance):
        return {"data": instance}
