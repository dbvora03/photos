# Generated by Django 3.0.8 on 2020-08-21 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200821_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='price2',
            new_name='pricetwo',
        ),
    ]
