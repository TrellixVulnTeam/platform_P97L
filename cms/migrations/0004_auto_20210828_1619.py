# Generated by Django 3.2.6 on 2021-08-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_cmssections_cms_regularity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmssections',
            name='cms_icon',
        ),
        migrations.AlterField(
            model_name='cmssections',
            name='cms_number',
            field=models.CharField(max_length=10, verbose_name='Колличество учащихся в группе (... - ...)'),
        ),
        migrations.AlterField(
            model_name='cmssections',
            name='cms_textDesc',
            field=models.TextField(max_length=200, verbose_name='Общая информация'),
        ),
        migrations.AlterField(
            model_name='cmssections',
            name='cms_textResult',
            field=models.TextField(max_length=100, verbose_name='Декларируемый результат'),
        ),
    ]
