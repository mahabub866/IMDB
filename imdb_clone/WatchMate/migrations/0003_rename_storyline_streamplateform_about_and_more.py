# Generated by Django 4.0.5 on 2022-06-26 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WatchMate', '0002_streamplateform_watchlist_delete_moive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamplateform',
            old_name='storyline',
            new_name='about',
        ),
        migrations.AddField(
            model_name='streamplateform',
            name='website',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
