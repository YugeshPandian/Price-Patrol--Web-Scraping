# Generated by Django 4.2.1 on 2023-05-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Websp', '0005_alter_offerboth_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerboth',
            name='amazon_url',
            field=models.URLField(max_length=750),
        ),
        migrations.AlterField(
            model_name='offerboth',
            name='flipkart_url',
            field=models.URLField(max_length=750),
        ),
    ]
