# Generated by Django 5.1.2 on 2024-11-19 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0018_remove_event_registration_deadline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportdetails',
            name='allowed_category',
        ),
        migrations.RemoveField(
            model_name='sportdetails',
            name='event',
        ),
        migrations.RemoveField(
            model_name='sportdetails',
            name='sport',
        ),
        migrations.AddField(
            model_name='sportdetails',
            name='team_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_details', to='ligameet.teamcategory'),
        ),
    ]
