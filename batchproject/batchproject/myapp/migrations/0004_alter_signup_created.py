# Generated by Django 3.2 on 2022-11-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_signup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]