# Generated by Django 4.1.2 on 2022-11-08 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cart", "0002_delete_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="cart",
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
                    "student_mail",
                    models.EmailField(
                        max_length=255,
                        null=True,
                        unique=True,
                        validators=[django.core.validators.EmailValidator()],
                        verbose_name="email address",
                    ),
                ),
                ("total_price", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]