# Generated by Django 2.2 on 2019-06-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20190619_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='created_at',
            field=models.CharField(default='', max_length=30, verbose_name='Дата создания уведомления'),
        ),
    ]
