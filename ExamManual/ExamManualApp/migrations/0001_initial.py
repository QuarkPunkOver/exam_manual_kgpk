# Generated by Django 5.1.5 on 2025-01-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('IDUser', models.AutoField(primary_key=True, serialize=False)),
                ('LastName', models.CharField(max_length=255)),
                ('FirstName', models.CharField(max_length=255)),
                ('Patronymic', models.CharField(blank=True, max_length=255, null=True)),
                ('Login', models.CharField(max_length=255, unique=True)),
                ('Password', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=1)),
                ('BirthDay', models.DateField()),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('NumberPassport', models.CharField(max_length=20)),
                ('SerialPassport', models.CharField(max_length=20)),
                ('Block', models.BooleanField(default=False)),
                ('FirstAuth', models.DateTimeField()),
                ('Role', models.CharField(max_length=50)),
                ('Addres', models.TextField()),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]
