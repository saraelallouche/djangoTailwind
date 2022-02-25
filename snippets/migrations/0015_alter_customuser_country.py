# Generated by Django 4.0.2 on 2022-02-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0014_remove_customuser_by_email_candidates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="country",
            field=models.CharField(
                choices=[("USA", "United states"), ("CA", "Canada"), ("FR", "France")],
                max_length=10,
            ),
        ),
    ]
