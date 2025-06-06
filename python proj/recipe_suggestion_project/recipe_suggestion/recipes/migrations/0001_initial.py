# Generated by Django 3.1.12 on 2025-05-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('steps', models.TextField()),
                ('cuisine', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/')),
            ],
        ),
    ]
