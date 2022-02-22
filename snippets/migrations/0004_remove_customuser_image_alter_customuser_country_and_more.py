# Generated by Django 4.0.2 on 2022-02-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0003_alter_customuser_country_alter_customuser_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="image",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="country",
            field=models.CharField(
                choices=[("0", "United states"), ("1", "Canada"), ("2", "France")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="notifications",
            field=models.CharField(
                choices=[
                    ("0", "Everything"),
                    ("1", "Same as email"),
                    ("2", "No push notifications"),
                ],
                default="",
                max_length=2,
            ),
        ),
    ]
