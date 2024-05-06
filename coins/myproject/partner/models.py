from django.db import models
from django.conf import settings

class Partner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    referral_link = models.CharField(max_length=255, verbose_name="Реферальная ссылка")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class Referral(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Партнер")
    referred_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Привлечённый пользователь")
    exchange_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма обмена")
    class Meta:
        verbose_name = "Реферал"
        verbose_name_plural = "Рефералы"
