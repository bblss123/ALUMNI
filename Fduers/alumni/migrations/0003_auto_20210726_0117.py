# Generated by Django 3.2.5 on 2021-07-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_auto_20210726_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='prov',
        ),
        migrations.AddField(
            model_name='user',
            name='prov_id',
            field=models.IntegerField(default=1, verbose_name='地域'),
            preserve_default=False,
        ),
    ]
