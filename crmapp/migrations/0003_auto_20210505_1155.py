# Generated by Django 3.1.6 on 2021-05-05 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_auto_20210502_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissions',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 5)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 5)),
        ),
    ]
