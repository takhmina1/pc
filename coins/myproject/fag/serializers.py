from rest_framework import serializers

class FAQSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()
