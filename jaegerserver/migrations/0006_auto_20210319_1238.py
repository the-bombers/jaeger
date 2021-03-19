# Generated by Django 3.1.7 on 2021-03-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaegerserver', '0005_merge_20210319_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='monsters',
        ),
        migrations.AlterField(
            model_name='monster',
            name='features',
            field=models.JSONField(default=['REDACTED']),
        ),
    ]