# Generated by Django 4.0.2 on 2022-02-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0005_customuser_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="image",
            field=models.ImageField(null=True, upload_to="media/"),
        ),
    ]
