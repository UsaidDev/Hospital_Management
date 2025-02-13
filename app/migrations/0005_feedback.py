# Generated by Django 5.0.7 on 2024-07-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_departments_dep_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patients_name', models.CharField(max_length=100)),
                ('patients_username', models.CharField(max_length=100)),
                ('patients_image', models.ImageField(upload_to='patients/')),
                ('patients_comments', models.TextField()),
            ],
        ),
    ]
