from rest_framework import serializers
from .models import Balance, Transac

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['user', 'currency', 'amount']

class TransacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transac
        fields = ['user', 'amount', 'timestamp']
