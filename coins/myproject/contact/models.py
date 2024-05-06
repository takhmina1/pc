from django.db import models
from django.utils import timezone
class Contact(models.Model):
    email = models.EmailField(verbose_name='Адрес электронной почты')
    website = models.URLField(verbose_name='Веб-сайт', blank=True, null=True)
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ChatMessage(models.Model):
    sender = models.EmailField(verbose_name='Отправитель')
    message = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='Временная метка')

    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чата'
