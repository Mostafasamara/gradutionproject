# Generated by Django 3.2 on 2022-05-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='upload',
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
