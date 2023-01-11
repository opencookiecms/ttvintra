# Generated by Django 4.0.4 on 2022-12-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labassets', '0004_rename_focallenth_lens_focallength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='itempic',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]