# Generated by Django 5.1.1 on 2025-01-03 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount_price',
            new_name='amount_paid',
        ),
    ]
