# Generated by Django 4.2.6 on 2024-03-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_num', models.CharField(max_length=100)),
                ('guard_relation', models.CharField(max_length=100)),
            ],
        ),
    ]
