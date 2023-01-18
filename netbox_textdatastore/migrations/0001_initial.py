# Generated by Django 4.0.7 on 2022-09-16 10:12

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0153_created_datetimefield'),
        ('extras', '0073_journalentry_tags_custom_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextDataObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(default='device config', max_length=100)),
                ('data', models.TextField(blank=True, default='')),
                ('hash', models.CharField(blank=True, default='', max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textdata', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('device', 'name'),
            },
        ),
    ]
