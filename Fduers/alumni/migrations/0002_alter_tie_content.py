# Generated by Django 3.2.5 on 2021-07-14 12:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tie',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
