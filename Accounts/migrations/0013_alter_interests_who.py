# Generated by Django 3.2.9 on 2021-12-22 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_alter_interests_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interests',
            name='who',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]