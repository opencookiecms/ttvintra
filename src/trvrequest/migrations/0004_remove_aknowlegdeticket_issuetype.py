# Generated by Django 4.0.4 on 2022-07-20 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trvrequest', '0003_remove_aknowlegdeticket_carchoose_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aknowlegdeticket',
            name='issuetype',
        ),
    ]
