from django.db import models
from django.conf import settings

class Discount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    total_transactions = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая сумма транзакций')
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2, default=0.08, verbose_name='Процент скидки')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    @classmethod
    def update_discount(cls, user, amount):
        user_discount, created = cls.objects.get_or_create(user=user)
        user_discount.total_transactions += amount
        user_discount.save()  # Сохраняем обновленную скидку

        if user_discount.total_transactions < 500:
            user_discount.discount_percentage = 0.08
        elif 500 <= user_discount.total_transactions < 1000:
            user_discount.discount_percentage = 0.1
        elif 1000 <= user_discount.total_transactions < 2000:
            user_discount.discount_percentage = 0.12
        elif 2000 <= user_discount.total_transactions < 4000:
            user_discount.discount_percentage = 0.14
        elif 4000 <= user_discount.total_transactions < 6000:
            user_discount.discount_percentage = 0.16
        elif 6000 <= user_discount.total_transactions < 10000:
            user_discount.discount_percentage = 0.18
        else:
            user_discount.discount_percentage = 0.2

        user_discount.save()  # Сохраняем обновленный процент скидки


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Discount.update_discount(self.user, self.amount)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
