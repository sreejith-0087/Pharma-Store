# Generated by Django 4.2.4 on 2023-09-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_orders_cart_user_productorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
            preserve_default=False,
        ),
    ]
