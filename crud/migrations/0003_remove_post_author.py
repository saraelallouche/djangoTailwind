# Generated by Django 4.0.2 on 2022-03-12 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0002_alter_post_body"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
    ]
