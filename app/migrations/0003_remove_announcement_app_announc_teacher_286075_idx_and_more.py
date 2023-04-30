# Generated by Django 4.2 on 2023-04-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='announcement',
            name='app_announc_teacher_286075_idx',
        ),
        migrations.AddIndex(
            model_name='announcement',
            index=models.Index(fields=['teacher_id', 'course_id'], name='app_announc_teacher_286075_idx'),
        ),
    ]