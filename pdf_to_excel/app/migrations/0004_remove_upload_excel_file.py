# Generated by Django 5.1.6 on 2025-02-08 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_upload_excel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='excel_file',
        ),
    ]
