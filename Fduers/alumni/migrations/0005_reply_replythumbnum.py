# Generated by Django 3.2.5 on 2021-07-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_reply_createdtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='replyThumbNum',
            field=models.IntegerField(default=0),
        ),
    ]
