# Generated by Django 2.0.3 on 2020-06-20 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ur',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
