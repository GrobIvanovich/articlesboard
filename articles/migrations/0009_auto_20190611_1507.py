# Generated by Django 2.2 on 2019-06-11 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20190611_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
    ]