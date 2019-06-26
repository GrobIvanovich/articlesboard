from django.db import models
from articles.models import AdvUser


class Message(models.Model):
    sender = models.CharField(max_length=50, default='', verbose_name='Отправитель')
    receiver = models.CharField(max_length=50, default='', verbose_name='Получатель')
    message = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата отправления')
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'