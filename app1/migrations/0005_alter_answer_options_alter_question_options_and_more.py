# Generated by Django 4.2.2 on 2023-06-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AlterField(
            model_name='answer',
            name='createDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='createDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]