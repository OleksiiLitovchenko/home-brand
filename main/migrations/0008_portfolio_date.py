# Generated by Django 4.2.8 on 2024-01-30 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_portfolio_descr'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.TextField(default=datetime.datetime(2024, 1, 30, 14, 47, 23, 371728), max_length=50),
        ),
    ]
