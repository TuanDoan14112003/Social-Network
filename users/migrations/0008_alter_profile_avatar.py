# Generated by Django 3.2.7 on 2021-09-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_level_profile_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='img/default_avatar.jpg', upload_to='user_pics'),
        ),
    ]
