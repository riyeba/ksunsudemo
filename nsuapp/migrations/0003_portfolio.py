# Generated by Django 3.2.24 on 2024-07-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsuapp', '0002_speech'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=350)),
                ('name', models.CharField(max_length=350)),
                ('department', models.CharField(max_length=350)),
                ('level', models.CharField(max_length=350)),
                ('mobile', models.CharField(max_length=350)),
              
            ],
        ),
    ]