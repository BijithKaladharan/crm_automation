# Generated by Django 3.1.6 on 2021-05-02 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissions',
            name='batch_code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='admissions',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 2)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 2)),
        ),
    ]
