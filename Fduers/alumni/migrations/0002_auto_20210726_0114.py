# Generated by Django 3.2.5 on 2021-07-26 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_auto_20210726_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.AddField(
            model_name='user',
            name='prov',
            field=models.CharField(default=1, max_length=20, verbose_name='地域'),
            preserve_default=False,
        ),
    ]
