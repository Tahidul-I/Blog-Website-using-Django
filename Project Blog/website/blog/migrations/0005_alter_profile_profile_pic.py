# Generated by Django 4.2.6 on 2023-10-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
