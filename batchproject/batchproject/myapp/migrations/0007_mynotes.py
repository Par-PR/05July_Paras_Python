# Generated by Django 3.2 on 2022-11-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_signup_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('querytitle', models.CharField(max_length=200)),
                ('cate', models.CharField(max_length=100)),
                ('myfile', models.FileField(upload_to='MyNotes')),
                ('comments', models.TextField()),
            ],
        ),
    ]
