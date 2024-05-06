from django.db import models
from django.conf import settings
from .choices import CURRENCY_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()
class Balance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Сумма')
    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

class Transac(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
