# Generated by Django 4.2.4 on 2023-08-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_v22', '0002_rename_passwords_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
