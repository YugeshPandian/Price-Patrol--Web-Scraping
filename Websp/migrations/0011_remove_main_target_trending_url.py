# Generated by Django 4.2.1 on 2023-06-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Websp', '0010_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='Target',
        ),
        migrations.AddField(
            model_name='trending',
            name='url',
            field=models.URLField(blank=True, max_length=750, null=True),
        ),
    ]