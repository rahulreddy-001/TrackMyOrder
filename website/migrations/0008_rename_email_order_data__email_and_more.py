# Generated by Django 4.0.5 on 2022-09-18 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_order_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_data',
            old_name='email',
            new_name='_email',
        ),
        migrations.RenameField(
            model_name='order_data',
            old_name='name',
            new_name='_name',
        ),
    ]
