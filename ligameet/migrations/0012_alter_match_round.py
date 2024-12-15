# Generated by Django 5.1.2 on 2024-12-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligameet', '0011_alter_match_score_team_a_alter_match_score_team_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='round',
            field=models.CharField(choices=[('First Round', 'First Round'), ('Quarter-finals', 'Quarter-finals'), ('Semi-finals', 'Semi-finals'), ('Finals', 'Finals'), ('Grand final', 'Grand final')], max_length=50, null=True),
        ),
    ]
