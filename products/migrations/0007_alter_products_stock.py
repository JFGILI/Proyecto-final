# Generated by Django 4.1.4 on 2023-01-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.BooleanField(),
        ),
    ]
