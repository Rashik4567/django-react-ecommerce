# Generated by Django 3.2 on 2021-04-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_product_third_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.FloatField(default=24.99),
            preserve_default=False,
        ),
    ]
