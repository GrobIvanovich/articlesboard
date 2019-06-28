from django.db import models
from articles.models import AdvUser
from datetime import datetime


class Dialog(models.Model):
    members = models.ManyToManyField(AdvUser, related_name='members', blank=True, verbose_name='Диалог')


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, verbose_name='Диалог', default=1)
    sender = models.CharField(max_length=50, default='', verbose_name='Отправитель')
    receiver = models.CharField(max_length=50, default='', verbose_name='Получатель')
    message = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата отправления')
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


    # content = models.ManyToManyField(Message, 'content', blank=True, verbose_name='Сообщения')    
