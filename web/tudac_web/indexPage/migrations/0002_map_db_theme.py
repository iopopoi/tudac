# Generated by Django 3.0.6 on 2020-06-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map_db',
            name='theme',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
