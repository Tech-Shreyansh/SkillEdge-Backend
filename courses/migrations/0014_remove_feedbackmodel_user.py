# Generated by Django 4.1.3 on 2022-11-14 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0013_course_weighted_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedbackmodel",
            name="user",
        ),
    ]