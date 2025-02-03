# Generated by Django 4.2.17 on 2025-02-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bar",
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
                ("name", models.CharField(max_length=64)),
                ("data", models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name="Pose",
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
                    "limb",
                    models.CharField(
                        choices=[
                            ("right-arm", "right-arm"),
                            ("left-arm", "left-arm"),
                            ("right-leg", "right-leg"),
                            ("left-leg", "left-leg"),
                            ("torso", "torso"),
                            ("facing", "facing"),
                        ],
                        max_length=16,
                    ),
                ),
                ("slug", models.CharField(max_length=16, unique=True)),
                ("name", models.CharField(max_length=16, unique=True)),
                ("description", models.TextField(blank=True, default="")),
            ],
        ),
    ]
