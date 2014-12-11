# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0005_alter_user_last_login_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attached',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('AttachName', models.CharField(max_length=50)),
                ('AttachedType', models.CharField(max_length=50)),
                ('AttachedPath', models.CharField(max_length=50)),
                ('AttachedSize', models.CharField(max_length=50)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='BlogGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('GroupName', models.CharField(max_length=80, unique=True)),
                ('Permissions', models.ManyToManyField(verbose_name='permissions', to='auth.Permission', blank=True)),
            ],
            options={
                'verbose_name': 'blog group',
                'verbose_name_plural': 'blog groups',
            },
            bases=None,
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('UserName', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=100, unique=True)),
                ('Avatar', models.URLField(blank=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('access_token', models.CharField(max_length=100, blank=True)),
                ('refresh_token', models.CharField(max_length=100, blank=True)),
                ('expires_in', models.BigIntegerField(max_length=100, default=0)),
                ('Groups', models.ManyToManyField(related_name='usergroup', to='blog.BlogGroup', blank=True)),
            ],
            options={
                'ordering': ('-Created_at',),
            },
            bases=None,
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=50)),
                ('CreateTime', models.DateTimeField(auto_now=True)),
                ('Children', models.ManyToManyField(related_name='Children_rel_+', to='blog.Category', blank=True)),
                ('CreateUser', models.ForeignKey(to='blog.BlogUser')),
                ('ParentId', models.ForeignKey(to='blog.Category', blank=True)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('briefText', models.TextField(max_length=50)),
                ('CommentText', models.TextField(max_length=5000)),
                ('CommentTime', models.DateTimeField(auto_now=True)),
                ('IPAddress', models.GenericIPAddressField()),
                ('UserAgent', models.CharField(max_length=50)),
                ('User', models.ForeignKey(to='blog.BlogUser')),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('SubTitle', models.CharField(max_length=50, blank=True)),
                ('AllowComment', models.BooleanField(default=True)),
                ('Abstract', models.CharField(max_length=400, blank=True)),
                ('ContentText', models.TextField(max_length=10000)),
                ('CreateTime', models.DateTimeField(auto_now=True)),
                ('LastModifyTime', models.DateTimeField(auto_now=True)),
                ('IPAddress', models.GenericIPAddressField()),
                ('UserAgent', models.CharField(max_length=50)),
                ('Attached', models.ManyToManyField(related_name='Attached', to='blog.Attached')),
                ('Category', models.ManyToManyField(related_name='Category', to='blog.Category')),
                ('Comment', models.ManyToManyField(related_name='Comment', to='blog.Comment')),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=20)),
            ],
            options=None,
            bases=None,
        ),
        migrations.AddField(
            model_name='post',
            name='PostType',
            field=models.ManyToManyField(related_name='PostType', to='blog.PostType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='auther',
            field=models.ForeignKey(to='blog.BlogUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='permissions',
            field=models.ManyToManyField(verbose_name='permissions', to='auth.Permission', blank=True),
            preserve_default=True,
        ),
    ]
