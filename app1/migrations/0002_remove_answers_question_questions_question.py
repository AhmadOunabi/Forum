# Generated by Django 4.0.6 on 2023-06-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.AddField(
            model_name='questions',
            name='question',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
