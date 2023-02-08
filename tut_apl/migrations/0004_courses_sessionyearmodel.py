# Generated by Django 4.1.5 on 2023-02-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tut_apl', '0003_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SessionYearModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
            ],
        ),
    ]
