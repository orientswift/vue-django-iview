# Generated by Django 2.1.2 on 2018-10-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181026_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='buy_price',
            field=models.FloatField(verbose_name='进货价'),
        ),
        migrations.AlterField(
            model_name='good',
            name='sale_price',
            field=models.FloatField(verbose_name='销售价'),
        ),
    ]