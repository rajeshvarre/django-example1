# Generated by Django 3.0.5 on 2020-06-26 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20200624_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=264, unique=True)),
                ('last', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]