# Generated by Django 5.0 on 2024-01-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0004_user_creation_date_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="course",
            field=models.CharField(
                choices=[("CSC 315", "CSC 315"), ("CSC 317", "CSC 317")], max_length=20
            ),
        ),
    ]
