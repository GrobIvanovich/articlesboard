from django.db import models
from articles.models import AdvUser


class Message(models.Model):
    sender = models.ForeignKey(AdvUser, on_delete=models.PROTECT, default=None, verbose_name='Отправитель', related_name='sender')
    receiver = models.ForeignKey(AdvUser, on_delete=models.PROTECT, default=None, verbose_name='Получатель', related_name='receiver')
    message = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата отправления')
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'