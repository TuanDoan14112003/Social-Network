# Generated by Django 3.2.7 on 2021-10-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagekit_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]