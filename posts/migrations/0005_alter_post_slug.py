# Generated by Django 4.1 on 2022-08-10 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]