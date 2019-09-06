# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-09-06 03:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0004_auto_20190905_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='dog',
            name='vaccinated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(verbose_name='Age in month'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(blank=True, max_length=255, verbose_name='Breed'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='image_filename',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(blank=True, choices=[('s', 'small'), ('m', 'medium'), ('l', 'large'), ('xl', 'xlarge')], max_length=2, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='userdog',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='pugorugh.Dog'),
        ),
        migrations.AlterField(
            model_name='userdog',
            name='status',
            field=models.CharField(choices=[('l', 'liked'), ('d', 'disliked'), ('u', 'undecided')], max_length=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='userdog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='age',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('b', 'baby'), ('y', 'young'), ('a', 'adult'), ('s', 'senior')], default='b,y,a,s', max_length=50),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('m', 'male'), ('f', 'female')], default='m,f', max_length=50),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large'), ('xl', 'xlarge')], default='s,m,l,xl', max_length=50),
        ),
        migrations.AlterField(
            model_name='userpref',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userdog',
            unique_together=set([('user', 'dog')]),
        ),
    ]
