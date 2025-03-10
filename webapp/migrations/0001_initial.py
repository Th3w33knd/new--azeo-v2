# Generated by Django 5.0.7 on 2024-07-31 17:43

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Participant",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_default=django.db.models.functions.datetime.Now(),
                    ),
                ),
                ("fname", models.CharField(max_length=50, verbose_name="First Name")),
                ("lname", models.CharField(max_length=50, verbose_name="Last Name")),
                ("email", models.EmailField(max_length=255)),
                ("phone", models.CharField(max_length=10, verbose_name="Phone No.")),
                (
                    "alt_phone",
                    models.CharField(
                        max_length=10, null=True, verbose_name="Alternate Phone No."
                    ),
                ),
                (
                    "curr_year",
                    models.PositiveSmallIntegerField(verbose_name="Current Year"),
                ),
                ("university", models.CharField(max_length=255)),
                ("address", models.TextField(max_length=300)),
                ("pincode", models.CharField(max_length=10)),
                ("state", models.CharField(max_length=25)),
            ],
        ),
    ]
