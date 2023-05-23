# Generated by Django 4.1.7 on 2023-05-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0016_rename_date_of_onboarding_user_date_for_your_onboarding"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="image",),
        migrations.AddField(
            model_name="user",
            name="referral_code",
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "Sme"),
                    (2, "Admin"),
                    (3, "Delivery"),
                    (4, "Retail_outlets"),
                    (5, "Residential"),
                ],
                default=5,
                null=True,
            ),
        ),
    ]