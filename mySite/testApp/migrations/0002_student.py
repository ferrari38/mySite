# Generated by Django 2.0.2 on 2018-02-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=16)),
                ('l_name', models.CharField(max_length=16)),
                ('school', models.IntegerField()),
                ('grade', models.IntegerField()),
            ],
        ),
    ]
