# Generated by Django 5.0 on 2024-11-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repotageModel', '0002_remove_repotagemodel_lat_remove_repotagemodel_long'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagmodel',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
        migrations.AlterField(
            model_name='repotagemodel',
            name='desc',
            field=models.TextField(max_length=10000, verbose_name='توضیحات'),
        ),
    ]
