# Generated by Django 4.0.1 on 2022-12-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0015_alter_cart_food_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='food_id',
            field=models.CharField(max_length=20),
        ),
    ]
