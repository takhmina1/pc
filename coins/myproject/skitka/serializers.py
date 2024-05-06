from rest_framework import serializers
from .models import Discount, Transaction

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['user', 'total_transactions', 'discount_percentage']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'timestamp']
