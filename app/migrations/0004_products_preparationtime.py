# Generated by Django 3.1.5 on 2021-01-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='preparationTime',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
