# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-04 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_intro',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='作者简介'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=128, null=True, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.URLField(blank=True, null=True, verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True, verbose_name='页数'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='副标题'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='译者'),
        ),
    ]