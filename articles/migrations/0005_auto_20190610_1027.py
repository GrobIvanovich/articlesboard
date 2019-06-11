# Generated by Django 2.2 on 2019-06-10 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_advuser_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Company', verbose_name='Компания'),
        ),
    ]
