# Generated by Django 4.2.1 on 2023-05-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Websp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferBoth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flipkart_url', models.URLField()),
                ('amazon_url', models.URLField()),
                ('buyprice', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Target', models.TextField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
