# Generated by Django 4.1.2 on 2022-10-31 13:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField()),
                ("is_solved", models.BooleanField(default=False)),
                ("solution", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "urgency",
                    models.CharField(
                        choices=[
                            ("High", "High"),
                            ("Average", "Average"),
                            ("Low", "Default"),
                        ],
                        default="Low",
                        max_length=20,
                    ),
                ),
                (
                    "department_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="departments.department",
                    ),
                ),
            ],
        ),
    ]