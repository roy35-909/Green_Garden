# Generated by Django 4.0.1 on 2022-12-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0019_cart_table_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='food_list',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]