# Generated by Django 3.0.8 on 2020-08-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(default='here', max_length=100),
            preserve_default=False,
        ),
    ]