# Generated by Django 3.2.5 on 2022-04-23 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20220423_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
