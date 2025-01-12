# Generated by Django 3.2.24 on 2024-07-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsuapp', '0009_upcomingevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activestudent',
            name='Emergency_FirstName',
        ),
        migrations.RemoveField(
            model_name='activestudent',
            name='Relationship',
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Address',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='College',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Degree',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Emergency_Surname',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='FamilyinSaudi',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='First_name',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Nextofkin_city',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Nextofkin_mobile',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Phone_number',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='Surname',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='auth_email',
            field=models.CharField(max_length=350, unique=True),
        ),
        migrations.AlterField(
            model_name='activestudent',
            name='auth_password',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='College',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Degree',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='First_name',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Graduation_year',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Occupation',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Phone_number',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Residence_Country',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Surname',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='auth_email',
            field=models.CharField(max_length=350, unique=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='auth_password',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='title',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='head',
            name='email',
            field=models.CharField(max_length=350, unique=True),
        ),
        migrations.AlterField(
            model_name='head',
            name='first_name',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='head',
            name='password',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='head',
            name='sur_name',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='recentevent',
            name='title',
            field=models.CharField(max_length=350),
        ),
    ]
