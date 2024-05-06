from django.db import models
class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор отзыва')
    content = models.TextField(verbose_name='Текст отзыва')
    date_posted = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
