# Generated by Django 4.0.2 on 2022-02-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0007_alter_customuser_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="media"),
        ),
    ]
