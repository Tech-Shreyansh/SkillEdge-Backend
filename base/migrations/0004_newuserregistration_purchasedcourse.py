# Generated by Django 4.1.2 on 2022-11-09 06:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_squashed_0003_rename_interest_newuserregistration_interested"),
    ]

    operations = [
        migrations.AddField(
            model_name="newuserregistration",
            name="purchasedCourse",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
