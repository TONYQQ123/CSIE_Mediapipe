# Generated by Django 4.2.10 on 2024-03-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybackend', '0002_account_born_account_distance_account_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='all_landmarks',
            field=models.JSONField(default=list, null=True),
        ),
    ]