# Generated by Django 4.1.7 on 2023-06-09 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("retailers", "0015_remove_manager_mobile_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="manager",
            options={"ordering": ("-date_created",)},
        ),
    ]