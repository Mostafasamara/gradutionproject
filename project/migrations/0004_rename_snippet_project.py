# Generated by Django 3.2.5 on 2022-04-23 03:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_alter_snippet_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Project',
        ),
    ]
