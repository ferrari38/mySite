# Generated by Django 2.0.2 on 2018-02-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_teacher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persons',
            new_name='Worker',
        ),
    ]
