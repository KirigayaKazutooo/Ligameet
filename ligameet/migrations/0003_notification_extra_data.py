# Generated by Django 5.0.1 on 2024-10-31 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0002_alter_event_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='extra_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
