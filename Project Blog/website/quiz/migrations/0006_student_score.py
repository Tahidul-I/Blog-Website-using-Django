# Generated by Django 4.2.6 on 2023-11-08 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0005_quiz_category_under_whom_alter_demoquiz_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(blank=True, max_length=500, null=True)),
                ('ques_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.make_quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
