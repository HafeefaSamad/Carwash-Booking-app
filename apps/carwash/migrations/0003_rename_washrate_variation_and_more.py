# Generated by Django 5.0.3 on 2024-03-28 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0002_rename_vehicletype_vehiclemodel_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WashRate',
            new_name='Variation',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='rate',
            new_name='price',
        ),
    ]