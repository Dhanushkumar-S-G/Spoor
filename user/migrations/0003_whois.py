# Generated by Django 4.1.4 on 2022-12-06 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_case_domain_alter_case_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="WhoIs",
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
                ("res", models.JSONField()),
                (
                    "case_number",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_whois_details",
                        to="user.case",
                    ),
                ),
            ],
        ),
    ]
