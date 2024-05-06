from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Cryptocurrency(models.Model):
    # Модель для криптовалюты, хранит информацию о ней
    name = models.CharField(max_length=100)  # Название криптовалюты
    currency_code = models.CharField(max_length=10)  # Код валюты
    symbol = models.CharField(max_length=10)  # Символьный код криптовалюты
    country = models.CharField(max_length=100)  # Страна
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)  # Курс обмена
    market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # Рыночная капитализация

    def __str__(self):
        return self.name

class FiatCurrency(models.Model):
    # Модель для фиатной валюты, хранит информацию о ней
    name = models.CharField(max_length=100)  # Название фиатной валюты
    currency_code = models.CharField(max_length=10)  # Код валюты
    symbol = models.CharField(max_length=10)  # Символьный код фиатной валюты
    country = models.CharField(max_length=100)  # Страна

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    # Профиль пользователя, хранит информацию о балансе и операциях с криптовалютой и фиатными деньгами
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile')  # Ссылка на пользователя
    balance = models.DecimalField(max_digits=20, decimal_places=2)  # Баланс пользователя

    def buy_crypto(self, cryptocurrency, amount, price_per_unit):
        # Метод для покупки криптовалюты
        total_cost = amount * price_per_unit
        commission = self.calculate_crypto_commission(total_cost)
        total_cost_with_commission = total_cost + commission

        # Проверяем достаточность средств на балансе пользователя
        if self.balance >= total_cost_with_commission:
            # Если достаточно средств, обновляем баланс и создаем транзакцию
            self.balance -= total_cost_with_commission
            self.save()
            Transaction.objects.create(user=self, transaction_type='buy_crypto', cryptocurrency=cryptocurrency, amount=amount, price=price_per_unit, commission=commission)
        else:
            raise ValueError("Недостаточно средств для покупки криптовалюты")

    def sell_crypto(self, cryptocurrency, amount, price_per_unit):
        # Метод для продажи криптовалюты
        total_gain = amount * price_per_unit
        commission = self.calculate_crypto_commission(total_gain)
        total_gain_after_commission = total_gain - commission

        # Обновляем баланс пользователя и сохраняем транзакцию
        self.balance += total_gain_after_commission
        self.save()
        Transaction.objects.create(user=self, transaction_type='sell_crypto', cryptocurrency=cryptocurrency, amount=amount, price=price_per_unit, commission=commission)

    def buy_fiat(self, fiat_currency, amount, price_per_unit):
        # Метод для покупки фиатных денег
        total_cost = amount * price_per_unit
        commission = self.calculate_fiat_commission(total_cost)
        total_cost_with_commission = total_cost + commission

        # Проверяем достаточность средств на балансе пользователя
        if self.balance >= total_cost_with_commission:
            # Если достаточно средств, обновляем баланс и создаем транзакцию
            self.balance -= total_cost_with_commission
            self.save()
            Transaction.objects.create(user=self, transaction_type='buy_fiat', fiat_currency=fiat_currency, amount=amount, price=price_per_unit, commission=commission)
        else:
            raise ValueError("Недостаточно средств для покупки фиатных денег")

    def sell_fiat(self, fiat_currency, amount, price_per_unit):
        # Метод для продажи фиатных денег
        total_gain = amount * price_per_unit
        commission = self.calculate_fiat_commission(total_gain)
        total_gain_after_commission = total_gain - commission

        # Обновляем баланс пользователя и сохраняем транзакцию
        self.balance += total_gain_after_commission
        self.save()
        Transaction.objects.create(user=self, transaction_type='sell_fiat', fiat_currency=fiat_currency, amount=amount, price=price_per_unit, commission=commission)

    def calculate_crypto_commission(self, total_amount):
        # Метод для расчета комиссии при покупке криптовалюты
        return total_amount * 0.01

    def calculate_fiat_commission(self, total_amount):
        # Метод для расчета комиссии при покупке фиатных денег
        return total_amount * 0.015

class CryptoWallet(models.Model):
    # Кошелек для хранения криптовалюты
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Ссылка на пользователя
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Ссылка на криптовалюту
    balance = models.DecimalField(max_digits=20, decimal_places=10)  # Баланс криптовалюты

    def __str__(self):
        return f'{self.user.username} - {self.cryptocurrency.name} Wallet'

class FiatWallet(models.Model):
    # Кошелек для хранения фиатных денег
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Ссылка на пользователя
    fiat_currency = models.ForeignKey(FiatCurrency, on_delete=models.CASCADE)  # Ссылка на фиатную валюту
    balance = models.DecimalField(max_digits=20, decimal_places=2)  # Баланс фиатных денег

    def __str__(self):
        return f'{self.user.username} - {self.fiat_currency.name} Wallet'

class Transaction(models.Model):
    # Транзакции пользователя
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Ссылка на профиль пользователя
    transaction_type = models.CharField(max_length=20)  # Тип транзакции
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, null=True, blank=True)  # Ссылка на криптовалюту (если есть)
    fiat_currency = models.ForeignKey(FiatCurrency, on_delete=models.CASCADE, null=True, blank=True)  # Ссылка на фиатную валюту (если есть)
    amount = models.DecimalField(max_digits=20, decimal_places=10)  # Сумма транзакции
    price = models.DecimalField(max_digits=20, decimal_places=10)  # Цена единицы криптовалюты/фиатной валюты
    commission = models.DecimalField(max_digits=20, decimal_places=10)  # Комиссия
    timestamp = models.DateTimeField(default=timezone.now)  # Временная метка транзакции

    def __str__(self):
        return f'{self.user.user.username} - {self.transaction_type}'
