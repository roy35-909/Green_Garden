# Generated by Django 4.0.1 on 2022-12-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0022_food_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='modifyed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
