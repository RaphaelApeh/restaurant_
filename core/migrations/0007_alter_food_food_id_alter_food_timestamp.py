# Generated by Django 5.1 on 2024-08-29 22:15

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_order_timestamp_alter_food_food_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.UUIDField(default=uuid.UUID('98e2f879-6e2e-44bf-9b97-c07589b3c61c'), unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 29, 23, 15, 52, 642003)),
        ),
    ]
