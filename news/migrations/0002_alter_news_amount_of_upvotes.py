# Generated by Django 3.2 on 2021-04-07 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="amount_of_upvotes",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(99)]
            ),
        ),
    ]
