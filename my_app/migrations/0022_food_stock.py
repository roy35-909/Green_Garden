# Generated by Django 4.0.1 on 2022-12-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0021_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
