# Generated by Django 4.1.4 on 2022-12-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destination",
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
                ("name", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                ("price", models.IntegerField()),
                ("img", models.ImageField(upload_to="pics")),
                ("offer", models.BooleanField(default=False)),
            ],
        ),
    ]
