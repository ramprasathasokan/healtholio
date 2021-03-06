# Generated by Django 3.0.2 on 2020-01-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicinalData', '0004_complaints'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dosage',
            name='duration',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dosage',
            name='time_of_day',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dosage',
            name='when',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='linktable',
            name='user_type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
