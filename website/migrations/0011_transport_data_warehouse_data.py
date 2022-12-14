# Generated by Django 4.0.5 on 2022-09-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_order_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_orderid', models.CharField(max_length=50)),
                ('_from', models.CharField(max_length=50)),
                ('_to', models.CharField(max_length=50)),
                ('_time', models.CharField(max_length=50)),
                ('_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_orderid', models.CharField(max_length=50)),
                ('_email', models.EmailField(max_length=50)),
                ('_from', models.CharField(max_length=50)),
                ('_to', models.CharField(max_length=50)),
                ('_status', models.CharField(max_length=50)),
                ('_time', models.CharField(max_length=50)),
                ('_size', models.CharField(max_length=50)),
            ],
        ),
    ]
