# Generated by Django 2.2 on 2019-06-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20190617_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='Было ли это уведомление отправлено пользователю?'),
        ),
    ]
