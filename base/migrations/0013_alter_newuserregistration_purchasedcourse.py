# Generated by Django 4.1.2 on 2022-11-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_feedbackmodel_sender"),
        ("base", "0012_alter_newuserregistration_purchasedcourse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuserregistration",
            name="purchasedCourse",
            field=models.ManyToManyField(to="courses.course"),
        ),
    ]