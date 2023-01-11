# Generated by Django 4.0.4 on 2022-12-29 05:29

from django.db import migrations, models
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    dependencies = [
        ('labassets', '0008_rename_createdat_cable_createdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='attachment',
            field=models.FileField(blank=True, null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='attachment/camera'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='itempic',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='photos/camera'),
        ),
        migrations.AlterField(
            model_name='lens',
            name='attachment',
            field=models.FileField(blank=True, null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='attachment/lens'),
        ),
        migrations.AlterField(
            model_name='lens',
            name='itempic',
            field=models.ImageField(blank=True, null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='photos/lens'),
        ),
    ]