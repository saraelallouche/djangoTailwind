# Generated by Django 4.0.2 on 2022-03-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0004_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="post-date"),
        ),
    ]
