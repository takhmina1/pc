from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=255, verbose_name='Название')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    purchase_date = models.DateField(verbose_name='Дата покупки')

    class Meta:
        verbose_name = "Инвестиция"
        verbose_name_plural = "Инвестиции"

class TradingStrategy(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = "Торговая стратегия"
        verbose_name_plural = "Торговые стратегии"

class Trade(models.Model):
    strategy = models.ForeignKey(TradingStrategy, on_delete=models.CASCADE, verbose_name="Стратегия")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, verbose_name="Инвестиция")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"
