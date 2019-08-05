from rest_framework import serializers


class LongAddSerializer(serializers.Serializer):
    number = serializers.IntegerField(required=True, min_value=10 ** 7)
