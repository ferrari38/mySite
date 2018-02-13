# Generated by Django 2.0.2 on 2018-02-11 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='myClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.IntegerField()),
                ('subject', models.IntegerField()),
                ('kind', models.IntegerField()),
                ('about', models.CharField(max_length=256)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.Teacher')),
            ],
        ),
    ]
