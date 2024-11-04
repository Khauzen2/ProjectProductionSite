from rest_framework import serializers

class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()