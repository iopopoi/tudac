# Generated by Django 3.0.6 on 2020-06-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexPage', '0002_map_db_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boring_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=128)),
            ],
        ),
    ]
