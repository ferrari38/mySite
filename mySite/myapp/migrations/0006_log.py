# Generated by Django 2.0.2 on 2018-02-11 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180211_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmp', models.IntegerField()),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Worker')),
            ],
        ),
    ]
