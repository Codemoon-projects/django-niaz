# Generated by Django 5.0 on 2025-01-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugstoresModel', '0002_alter_citymodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugstoresmodel',
            name='phone1',
            field=models.IntegerField(verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='drugstoresmodel',
            name='phone2',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره تماس'),
        ),
    ]
