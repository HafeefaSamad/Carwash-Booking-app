# Generated by Django 5.0.3 on 2024-03-27 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VehicleType',
            new_name='VehicleModel',
        ),
        migrations.RemoveField(
            model_name='washrate',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='washrate',
            name='vehicle_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carwash.vehiclemodel'),
            preserve_default=False,
        ),
    ]
