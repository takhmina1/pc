from rest_framework import serializers
from .models import Cryptocurrency, FiatCurrency, UserProfile, CryptoWallet, FiatWallet, Transaction

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'

class FiatCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FiatCurrency
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'balance']

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance

class CryptoWalletSerializer(serializers.ModelSerializer):
    cryptocurrency = CryptocurrencySerializer()

    class Meta:
        model = CryptoWallet
        fields = ['user', 'cryptocurrency', 'balance']

    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("Баланс не может быть отрицательным")
        return value

class FiatWalletSerializer(serializers.ModelSerializer):
    fiat_currency = FiatCurrencySerializer()

    class Meta:
        model = FiatWallet
        fields = ['user', 'fiat_currency', 'balance']

    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("Баланс не может быть отрицательным")
        return value

class TransactionSerializer(serializers.ModelSerializer):
    cryptocurrency = CryptocurrencySerializer(required=False)
    fiat_currency = FiatCurrencySerializer(required=False)

    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Сумма транзакции должна быть положительной")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительной")
        return value

    def validate_commission(self, value):
        if value < 0:
            raise serializers.ValidationError("Комиссия не может быть отрицательной")
        return value


# В skitka/serializers.py
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        ref_name = 'SkitkaTransaction'  # Явное указание ref_name

# В trading/serializers.py
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        ref_name = 'TradingTransaction'  # Явное указание ref_name





