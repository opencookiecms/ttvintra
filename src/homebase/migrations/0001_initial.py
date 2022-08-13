# Generated by Django 4.0.7 on 2022-08-13 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(blank=True, max_length=20, null=True)),
                ('givename', models.CharField(blank=True, max_length=150, null=True)),
                ('displayname', models.CharField(blank=True, max_length=150, null=True)),
                ('mailaddress', models.CharField(blank=True, max_length=150, null=True)),
                ('offid', models.CharField(blank=True, max_length=250, null=True)),
                ('subid', models.CharField(blank=True, max_length=250, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('userstatus', models.CharField(blank=True, max_length=50, null=True)),
                ('supervisor1', models.CharField(blank=True, max_length=100, null=True)),
                ('supervisor2', models.CharField(blank=True, max_length=100, null=True)),
                ('supervisor3', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialname', models.CharField(blank=True, max_length=150, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('linkup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homebase.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationPerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelrequest', models.BooleanField()),
                ('shipmentrequest', models.BooleanField()),
                ('ncar', models.BooleanField()),
                ('userlink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homebase.userprofile')),
            ],
        ),
    ]
