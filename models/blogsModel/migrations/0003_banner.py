# Generated by Django 5.0 on 2025-01-18 11:58

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsModel', '0002_alter_blogsmodel_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('name', models.CharField(max_length=100, verbose_name='نام بنر')),
                ('image', models.ImageField(upload_to='', verbose_name='بنر های پیشنهاد ویژه')),
            ],
            options={
                'verbose_name': 'بنر صفحه اصلی',
                'verbose_name_plural': 'بنر صفحه اصلی',
            },
        ),
    ]
