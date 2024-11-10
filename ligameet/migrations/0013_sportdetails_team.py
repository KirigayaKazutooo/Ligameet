# Generated by Django 5.1.2 on 2024-11-10 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0012_rename_sportrequirement_sportdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportdetails',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sport_details', to='ligameet.team'),
        ),
    ]
