# Generated by Django 5.1.5 on 2025-01-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManualApp', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
