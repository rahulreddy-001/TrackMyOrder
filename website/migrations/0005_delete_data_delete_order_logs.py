# Generated by Django 4.0.5 on 2022-09-17 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_utility_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.DeleteModel(
            name='Order_logs',
        ),
    ]