# Generated by Django 4.2.1 on 2023-06-05 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Websp', '0009_alter_scrapeddata_amazon_mrp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flipkart_url', models.URLField(max_length=750)),
                ('amazon_url', models.URLField(max_length=750)),
                ('buyprice', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Target', models.TextField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
