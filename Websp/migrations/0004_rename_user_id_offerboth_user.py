# Generated by Django 4.2.1 on 2023-05-29 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Websp', '0003_offerboth_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerboth',
            old_name='user_id',
            new_name='user',
        ),
    ]
