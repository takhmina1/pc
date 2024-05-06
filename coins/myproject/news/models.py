from django.db import models

class CurrencyNews(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='currency_news/', verbose_name='Изображение', blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость о валюте'
        verbose_name_plural = 'Новости о валютах'
