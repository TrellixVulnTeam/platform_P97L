# Generated by Django 3.2.6 on 2021-08-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_cmssections_cms_titlemodal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmssections',
            name='cms_durationH',
            field=models.CharField(default='', max_length=2, verbose_name='Продолжительность урока в академических часах'),
        ),
        migrations.AddField(
            model_name='cmssections',
            name='cms_regularity',
            field=models.CharField(default='', max_length=1, verbose_name='Колличество уроков в неделю'),
        ),
        migrations.AddField(
            model_name='cmssections',
            name='cms_termMonths',
            field=models.CharField(default='', max_length=2, verbose_name='Срок обучния (мес.)'),
        ),
        migrations.AddField(
            model_name='cmssections',
            name='cms_termTimes',
            field=models.CharField(default='', max_length=4, verbose_name='Колличество уроков в программе'),
        ),
    ]
