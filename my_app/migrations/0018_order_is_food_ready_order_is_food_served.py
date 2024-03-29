# Generated by Django 4.0.1 on 2022-12-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_alter_cart_food_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_food_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_food_served',
            field=models.BooleanField(default=False),
        ),
    ]
