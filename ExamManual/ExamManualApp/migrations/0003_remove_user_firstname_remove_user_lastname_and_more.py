# Generated by Django 5.1.5 on 2025-01-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManualApp', '0002_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Password',
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
