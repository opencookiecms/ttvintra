# Generated by Django 4.0.4 on 2022-12-08 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labassets', '0002_caltarget_quantity_card_quantity_misc_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cable',
            name='quantityaval',
        ),
    ]
