# Generated by Django 2.2 on 2019-06-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0057_auto_20190603_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='one_letter_name',
            field=models.CharField(default=None, max_length=1, unique=True, verbose_name='Название пола в одну букву. Используется в коде.'),
        ),
    ]