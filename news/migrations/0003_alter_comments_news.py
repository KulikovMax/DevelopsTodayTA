# Generated by Django 3.2 on 2021-04-08 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_news_amount_of_upvotes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="news",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="news.news",
            ),
        ),
    ]
