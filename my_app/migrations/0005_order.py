# Generated by Django 4.0.1 on 2022-12-09 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_day_feedback_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.CharField(max_length=15)),
                ('order_table', models.IntegerField()),
                ('is_payment_done', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
