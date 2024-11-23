# Generated by Django 5.0.1 on 2024-11-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0029_match_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EVENT_STATUS',
            field=models.CharField(choices=[('Draft', 'Draft'), ('open', 'Open For Registration'), ('ongoing', 'Ongoing'), ('finished', 'Finished'), ('cancelled', 'Cancelled')], default='Draft', max_length=21),
        ),
    ]