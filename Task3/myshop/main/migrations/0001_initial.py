# Generated by Django 4.2.11 on 2024-09-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("customers", models.CharField(max_length=255)),
                ("order_date", models.DateTimeField()),
                ("status", models.CharField(max_length=20)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
