# Generated by Django 2.1.2 on 2018-11-03 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_todo_due'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='title',
        ),
    ]
