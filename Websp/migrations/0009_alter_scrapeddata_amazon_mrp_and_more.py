# Generated by Django 4.2.1 on 2023-06-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Websp', '0008_alter_scrapeddata_flipkart_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeddata',
            name='amazon_mrp',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='scrapeddata',
            name='amazon_price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='scrapeddata',
            name='amazon_star',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='scrapeddata',
            name='flipkart_mrp',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='scrapeddata',
            name='flipkart_price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='scrapeddata',
            name='flipkart_star',
            field=models.TextField(),
        ),
    ]
