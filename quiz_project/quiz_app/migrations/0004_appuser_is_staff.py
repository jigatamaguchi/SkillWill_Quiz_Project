# Generated by Django 4.2.8 on 2023-12-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_remove_appuser_is_active_remove_appuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
