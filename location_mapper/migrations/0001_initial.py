# Generated by Django 4.2.4 on 2023-09-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("custom_name", models.CharField(max_length=255, unique=True)),
                ("google_maps_url", models.URLField()),
            ],
        ),
    ]