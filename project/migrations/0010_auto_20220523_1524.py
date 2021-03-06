# Generated by Django 3.2 on 2022-05-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_image_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('bio', models.CharField(default='', max_length=10000)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('email_token_time', models.DateTimeField(blank=True, null=True)),
                ('email_token', models.CharField(default='', max_length=64)),
                ('password_token_time', models.DateTimeField(blank=True, null=True)),
                ('password_token', models.CharField(default='', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='task',
            name='member',
            field=models.ManyToManyField(blank=True, related_name='members', to='project.User'),
        ),
    ]
