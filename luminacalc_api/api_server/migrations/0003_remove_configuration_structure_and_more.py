# Generated by Django 5.0.3 on 2024-03-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_rename_structure_construction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='structure',
        ),
        migrations.AddField(
            model_name='configuration',
            name='constructions',
            field=models.ManyToManyField(related_name='configurations', to='api_server.construction'),
        ),
    ]
