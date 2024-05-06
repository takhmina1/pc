from django.db import models
from django.utils.translation import gettext_lazy as _


class KYCAMLCheck(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    text = models.TextField(verbose_name=_('Текст'))

    class Meta:
        verbose_name = _('KYC/AML Запись')
        verbose_name_plural = _('KYC/AML Записи')
