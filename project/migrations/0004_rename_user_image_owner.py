# Generated by Django 3.2 on 2022-05-23 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='owner',
        ),
    ]
