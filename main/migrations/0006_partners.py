# Generated by Django 4.2.8 on 2024-01-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_about_options_alter_portfolio_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='partner/')),
                ('url', models.URLField(blank=True, default='')),
            ],
        ),
    ]