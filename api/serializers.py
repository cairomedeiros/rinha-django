from rest_framework import serializers

class PaymentsSerializer(serializers.Serializer):
    correlationId = serializers.UUIDField()
    amount = serializers.FloatField()
    requestedAt = serializers.DateTimeField()