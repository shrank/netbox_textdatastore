# Generated by Django 5.0.10 on 2024-12-17 12:25

import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_textdatastore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textdataobject',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
    ]
