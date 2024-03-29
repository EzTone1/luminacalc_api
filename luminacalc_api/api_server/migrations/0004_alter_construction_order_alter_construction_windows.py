# Generated by Django 5.0.3 on 2024-03-16 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0003_remove_configuration_structure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='construction', to='api_server.order'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='windows',
            field=models.ManyToManyField(related_name='construction', to='api_server.window'),
        ),
    ]
