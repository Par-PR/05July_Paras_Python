# Generated by Django 3.2 on 2022-11-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(),
        ),
    ]