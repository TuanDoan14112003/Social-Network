# Generated by Django 3.2.7 on 2021-09-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
        ('users', '0005_profile_point_origins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='point',
            new_name='total_point',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='point_origins',
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.channel')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
