from rest_framework import serializers
from .models import CurrencyRequest

class CurrencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRequest
        fields = ['id', 'number', 'date', 'direction', 'currency', 'status']
