# Generated by Django 3.0.8 on 2020-07-14 17:08

from django.db import migrations, models
import managevet.models


class Migration(migrations.Migration):

    dependencies = [
        ('managevet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinationhistory',
            name='petpic',
        ),
        migrations.AlterField(
            model_name='owner',
            name='ownername',
            field=models.CharField(max_length=100, verbose_name='Owner Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cellphone',
            field=models.CharField(blank=True, max_length=30, verbose_name='Cell Number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='employer',
            field=models.CharField(blank=True, max_length=100, verbose_name='Employer'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='familyvet',
            field=models.CharField(blank=True, max_length=100, verbose_name='Family Veterinarian'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hearaboutus',
            field=models.CharField(choices=[('Google', 'Google'), ('Yellow Pages', 'Yellow Pages'), ('Walk-in', 'Walk-in'), ('Other', 'Other')], default='Google', max_length=30, verbose_name='Heard From'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refvet',
            field=models.CharField(blank=True, max_length=100, verbose_name='Referring Veterinarian'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='workphone',
            field=models.CharField(blank=True, max_length=30, verbose_name='Work Phone'),
        ),
        migrations.AlterField(
            model_name='vaccinationhistory',
            name='current_medication',
            field=models.TextField(verbose_name='What medications is your pet currently receiving?'),
        ),
        migrations.AlterField(
            model_name='vaccinationhistory',
            name='howmuch_howoften_eat',
            field=models.CharField(max_length=100, verbose_name='Approximately how much and how often does your pet eat?'),
        ),
        migrations.AlterField(
            model_name='vaccinationhistory',
            name='normally_eat',
            field=models.CharField(max_length=100, verbose_name='What does your pet eat normally?'),
        ),
        migrations.AlterField(
            model_name='vaccinationhistory',
            name='primary_concern',
            field=models.TextField(verbose_name='What is your primary concern about your pet?'),
        ),
        migrations.AlterField(
            model_name='vaccinationhistory',
            name='vaccination_history',
            field=models.FileField(blank=True, upload_to=managevet.models.VaccinationHistory.petfile_path, verbose_name='Vaccination History File'),
        ),
    ]
