from rest_framework import serializers
from .models import ExchangeRule  # Предположим, что у вас есть модель ExchangeRule


class ExchangeRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRule  # Убедитесь, что ExchangeRule существует
        fields = '__all__'