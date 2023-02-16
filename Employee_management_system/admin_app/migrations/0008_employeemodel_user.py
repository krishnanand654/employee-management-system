# Generated by Django 4.1.5 on 2023-02-12 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_app', '0007_remove_leaveapplication_number_of_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
