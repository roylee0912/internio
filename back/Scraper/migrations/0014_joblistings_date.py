# Generated by Django 4.1.11 on 2023-10-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Scraper", "0013_remove_joblistings_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="joblistings",
            name="date",
            field=models.CharField(default="", max_length=500),
        ),
    ]