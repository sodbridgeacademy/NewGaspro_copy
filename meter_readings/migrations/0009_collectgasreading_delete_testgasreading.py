# Generated by Django 4.1.7 on 2023-05-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meter_readings", "0008_alter_activatedreading_smart_box"),
    ]

    operations = [
        migrations.CreateModel(
            name="CollectGasReading",
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
                    "smart_box_id",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("total_quantity_used", models.FloatField(blank=True, null=True)),
                ("quantity_remaining", models.FloatField(blank=True, null=True)),
                (
                    "battery_remaining",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "longitude",
                    models.CharField(blank=True, default="0", max_length=20, null=True),
                ),
                (
                    "latitude",
                    models.CharField(blank=True, default="0", max_length=20, null=True),
                ),
                ("last_push", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(name="TestGasReading",),
    ]