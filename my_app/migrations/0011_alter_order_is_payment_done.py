# Generated by Django 4.0.1 on 2022-12-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_day_total_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_payment_done',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]