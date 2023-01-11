# Generated by Django 4.0.4 on 2022-12-23 15:47

from django.db import migrations, models
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    dependencies = [
        ('labassets', '0007_alter_camera_attachment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cable',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='cable',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='caltarget',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='caltarget',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='camera',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='camera',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='laser',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='laser',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='lens',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='lens',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='lighting',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='lighting',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='lightingcon',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='lightingcon',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='misc',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='misc',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='optic',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='optic',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.RenameField(
            model_name='powersupply',
            old_name='createdat',
            new_name='createdate',
        ),
        migrations.RenameField(
            model_name='powersupply',
            old_name='updatedat',
            new_name='updatedate',
        ),
        migrations.AlterField(
            model_name='camera',
            name='attachment',
            field=models.FileField(blank=True, null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='attachment'),
        ),
    ]