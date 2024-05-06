from django.db import models
from .choices import CURRENCY_CHOICES, STATUS_CHOICES

class CurrencyRequest(models.Model):
    number = models.CharField(max_length=20, verbose_name='Номер')
    date = models.DateField(verbose_name='Дата')
    direction = models.CharField(max_length=100, verbose_name='Направление')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')

    class Meta:
        verbose_name = 'Заявка валюты'
        verbose_name_plural = 'Заявки валюты'

    def __str__(self):
        return f"Заявка {self.number}, {self.direction}"
