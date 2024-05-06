from django.db import models

class ExchangeRule(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Правило обмена"
        verbose_name_plural = "Правила обмена"
