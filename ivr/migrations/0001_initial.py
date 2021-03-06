# Generated by Django 3.0.5 on 2020-04-21 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=50)),
                ('caller_number', models.CharField(max_length=20)),
                ('dtmfDigits', models.CharField(max_length=10)),
                ('recordingUrl', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserBankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=30)),
                ('deposit', models.CharField(max_length=30)),
                ('withdrawal', models.CharField(max_length=30)),
                ('account_balance', models.CharField(max_length=30)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ivr.User')),
            ],
        ),
    ]
