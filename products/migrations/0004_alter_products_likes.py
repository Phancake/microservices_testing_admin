# Generated by Django 4.2.5 on 2023-09-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
