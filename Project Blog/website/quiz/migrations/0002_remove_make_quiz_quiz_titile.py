# Generated by Django 4.2.6 on 2023-10-28 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make_quiz',
            name='quiz_titile',
        ),
    ]
