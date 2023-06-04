# Generated by Django 4.1.7 on 2023-06-03 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("asset", "0027_rename_retailassigncylinder_residentialassigncylinder"),
        ("orders", "0002_bottleswaporder"),
    ]

    operations = [
        migrations.CreateModel(
            name="RefillOrder",
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
                    "quantity_remaining",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("pending", "pending"),
                            ("approved", "approved"),
                            ("ongoing", "ongoing"),
                            ("delivered", "delivered"),
                        ],
                        max_length=20,
                    ),
                ),
                ("transaction_id", models.CharField(blank=True, max_length=200)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "cylinder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cylinders",
                        to="asset.cylinder",
                    ),
                ),
                (
                    "smart_box",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meters",
                        to="asset.smartbox",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date_created"],
            },
        ),
        migrations.DeleteModel(
            name="BottleSwapOrder",
        ),
    ]
