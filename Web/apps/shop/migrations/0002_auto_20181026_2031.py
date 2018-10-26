# Generated by Django 2.1.2 on 2018-10-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_id', models.CharField(db_index=True, max_length=100, verbose_name='条码')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('genre', models.CharField(max_length=100, verbose_name='类别')),
                ('buy_price', models.IntegerField(verbose_name='进货价')),
                ('sale_price', models.IntegerField(verbose_name='销售价')),
                ('supplier', models.CharField(blank=True, max_length=200, null=True, verbose_name='供货商')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'shop_good',
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]
