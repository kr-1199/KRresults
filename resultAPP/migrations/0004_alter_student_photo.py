# Generated by Django 5.1.6 on 2025-04-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultAPP', '0003_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='student_photos/'),
        ),
    ]
