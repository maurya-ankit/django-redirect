# Generated by Django 3.1.1 on 2020-09-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usershort'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorten',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usershort',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
