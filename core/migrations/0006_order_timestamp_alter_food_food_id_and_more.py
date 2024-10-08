# Generated by Django 5.1 on 2024-08-29 21:33

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_food_food_id_alter_food_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 8, 29, 21, 33, 39, 696368, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.UUIDField(default=uuid.UUID('c789bd80-70f1-42b3-b358-079db39d4b71'), unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 29, 22, 33, 24, 19429)),
        ),
    ]
