# Generated by Django 4.2.2 on 2023-06-07 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='app1.question'),
            preserve_default=False,
        ),
    ]