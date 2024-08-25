# Generated by Django 5.1 on 2024-08-24 21:02

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_id',
            field=models.UUIDField(default=uuid.UUID('ad0f3f1b-b64b-4da4-8497-31de1582f70e')),
        ),
        migrations.AlterField(
            model_name='food',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 24, 22, 2, 3, 538430)),
        ),
    ]
