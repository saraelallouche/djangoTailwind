# Generated by Django 4.0.2 on 2022-03-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0003_remove_post_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
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
                    "file",
                    models.FileField(
                        default=None, upload_to="file/", verbose_name="file"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("USA", "United states"),
                            ("CA", "Canada"),
                            ("FR", "France"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
