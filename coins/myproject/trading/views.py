from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, CryptoWallet, FiatWallet, Cryptocurrency, FiatCurrency, Transaction
from .serializers import TransactionSerializer
from .services import get_user_profile, get_crypto_wallet, get_fiat_wallet, get_cryptocurrency_by_id, get_fiat_currency_by_id, create_transaction

# Класс для обработки запросов на покупку криптовалюты
class BuyCryptoAPIView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    # Метод, выполняемый при создании нового объекта через POST запрос
    def perform_create(self, serializer):
        # Получение профиля пользователя из запроса
        user_profile = get_user_profile(self.request.user)
        # Получение идентификатора криптовалюты из данных запроса
        cryptocurrency_id = serializer.validated_data['cryptocurrency']
        # Получение объекта криптовалюты по идентификатору
        cryptocurrency = get_cryptocurrency_by_id(cryptocurrency_id)
        # Извлечение данных о количестве и цене из запроса
        amount = serializer.validated_data['amount']
        price_per_unit = serializer.validated_data['price']
        # Рассчет комиссии исходя из профиля пользователя
        commission = user_profile.calculate_crypto_commission(amount * price_per_unit)
        # Получение криптовалютного кошелька пользователя для выбранной криптовалюты
        crypto_wallet = get_crypto_wallet(user_profile, cryptocurrency)
        # Проверка наличия достаточного количества средств на кошельке
        if crypto_wallet.balance < amount:
            raise serializers.ValidationError({'error': 'Insufficient funds in the cryptocurrency wallet'})
        # Создание транзакции покупки криптовалюты
        transaction = create_transaction(user_profile, 'buy_crypto', cryptocurrency=cryptocurrency, amount=amount, price=price_per_unit, commission=commission)
        # Обновление баланса криптовалютного кошелька
        crypto_wallet.balance -= amount
        crypto_wallet.save()
        # Обновление баланса пользователя
        user_profile.balance -= amount * price_per_unit + commission
        user_profile.save()

# Класс для обработки запросов на продажу криптовалюты
class SellCryptoAPIView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        user_profile = get_user_profile(self.request.user)
        cryptocurrency_id = serializer.validated_data['cryptocurrency']
        cryptocurrency = get_cryptocurrency_by_id(cryptocurrency_id)
        amount = serializer.validated_data['amount']
        price_per_unit = serializer.validated_data['price']
        commission = user_profile.calculate_crypto_commission(amount * price_per_unit)
        crypto_wallet = get_crypto_wallet(user_profile, cryptocurrency)
        transaction = create_transaction(user_profile, 'sell_crypto', cryptocurrency=cryptocurrency, amount=amount, price=price_per_unit, commission=commission)
        crypto_wallet.balance += amount
        crypto_wallet.save()
        user_profile.balance += amount * price_per_unit - commission
        user_profile.save()

# Класс для обработки запросов на покупку фиатной валюты
class BuyFiatAPIView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        user_profile = get_user_profile(self.request.user)
        fiat_currency_id = serializer.validated_data['fiat_currency']
        fiat_currency = get_fiat_currency_by_id(fiat_currency_id)
        amount = serializer.validated_data['amount']
        price_per_unit = serializer.validated_data['price']
        commission = user_profile.calculate_fiat_commission(amount * price_per_unit)
        fiat_wallet = get_fiat_wallet(user_profile, fiat_currency)
        if fiat_wallet.balance < amount * price_per_unit + commission:
            raise serializers.ValidationError({'error': 'Insufficient funds in the fiat wallet'})
        transaction = create_transaction(user_profile, 'buy_fiat', fiat_currency=fiat_currency, amount=amount, price=price_per_unit, commission=commission)
        fiat_wallet.balance -= amount * price_per_unit + commission
        fiat_wallet.save()
        user_profile.balance += amount
        user_profile.save()

# Класс для обработки запросов на продажу фиатной валюты
class SellFiatAPIView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        user_profile = get_user_profile(self.request.user)
        fiat_currency_id = serializer.validated_data['fiat_currency']
        fiat_currency = get_fiat_currency_by_id(fiat_currency_id)
        amount = serializer.validated_data['amount']
        price_per_unit = serializer.validated_data['price']
        commission = user_profile.calculate_fiat_commission(amount * price_per_unit)
        fiat_wallet = get_fiat_wallet(user_profile, fiat_currency)
        transaction = create_transaction(user_profile, 'sell_fiat', fiat_currency=fiat_currency, amount=amount, price=price_per_unit, commission=commission)
        fiat_wallet.balance += amount
        fiat_wallet.save()
        user_profile.balance += amount * price_per_unit - commission
        user_profile.save()
