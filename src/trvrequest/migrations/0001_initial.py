# Generated by Django 4.0.4 on 2023-02-09 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travelinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offid', models.CharField(blank=True, max_length=200, null=True)),
                ('companyname', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('emailname', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('travelpurpose', models.CharField(blank=True, max_length=200, null=True)),
                ('customername', models.CharField(blank=True, max_length=100, null=True)),
                ('projectcode', models.CharField(blank=True, max_length=20, null=True)),
                ('destinations', models.CharField(blank=True, max_length=150, null=True)),
                ('datearrive', models.DateField(blank=True, null=True)),
                ('datereturn', models.DateField(blank=True, null=True)),
                ('timearrive', models.CharField(blank=True, max_length=20, null=True)),
                ('timereturn', models.CharField(blank=True, max_length=20, null=True)),
                ('transport', models.CharField(blank=True, max_length=20, null=True)),
                ('airlinepreferred', models.CharField(blank=True, max_length=10, null=True)),
                ('seatingpreferred', models.CharField(blank=True, max_length=10, null=True)),
                ('luggageneeded', models.CharField(blank=True, max_length=10, null=True)),
                ('luggageweight', models.CharField(blank=True, max_length=10, null=True)),
                ('luggagereason', models.CharField(blank=True, max_length=200, null=True)),
                ('hotelneeded', models.CharField(blank=True, max_length=10, null=True)),
                ('numbernights', models.CharField(blank=True, max_length=10, null=True)),
                ('hotellocation', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('hodstatus', models.CharField(blank=True, max_length=10, null=True)),
                ('drstatus', models.CharField(blank=True, max_length=10, null=True)),
                ('hodapproval', models.CharField(blank=True, max_length=150, null=True)),
                ('hodemail', models.CharField(blank=True, max_length=150, null=True)),
                ('directorapproval', models.CharField(blank=True, max_length=150, null=True)),
                ('dremail', models.CharField(blank=True, max_length=150, null=True)),
                ('createby', models.CharField(blank=True, max_length=150, null=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AknowlegdeTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport', models.CharField(blank=True, max_length=50, null=True)),
                ('issuetref', models.CharField(blank=True, max_length=150, null=True)),
                ('issuetdate', models.DateField(blank=True, null=True)),
                ('issuelink', models.CharField(blank=True, max_length=250, null=True)),
                ('issuefile', models.FileField(blank=True, null=True, upload_to='')),
                ('createby', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issuerelate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trvrequest.travelinfo')),
            ],
        ),
    ]
