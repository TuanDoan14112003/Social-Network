# Generated by Django 3.2.7 on 2021-09-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profile_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]