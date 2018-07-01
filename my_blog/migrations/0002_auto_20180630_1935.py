# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='文章',
        ),
        migrations.AlterModelTable(
            name='articledetail',
            table='文章详情',
        ),
        migrations.AlterModelTable(
            name='blog',
            table='博客设置信息',
        ),
        migrations.AlterModelTable(
            name='category',
            table='自定义分类',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='用户评论',
        ),
        migrations.AlterModelTable(
            name='poll',
            table='用户点赞',
        ),
        migrations.AlterModelTable(
            name='sitecate',
            table='网站文章分类',
        ),
        migrations.AlterModelTable(
            name='sitecatedetail',
            table='网站详细分类',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='用户信息',
        ),
    ]
