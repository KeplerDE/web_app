# Generated by Django 4.0.3 on 2022-04-01 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_users_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_wishlist',
        ),
    ]
