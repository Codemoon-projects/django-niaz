# Generated by Django 5.0 on 2024-11-23 09:29

import django.core.validators
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusers',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='allusers',
            name='username',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(9000000000), django.core.validators.MaxValueValidator(9999999999)], verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='karfarmamodel',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='karfarmamodel',
            name='date',
            field=django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ تاسیس'),
        ),
        migrations.AlterField(
            model_name='karjomodel',
            name='created_at',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد'),
        ),
    ]
