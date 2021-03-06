# Generated by Django 3.2.5 on 2021-07-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_question_rightchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='used',
            field=models.BooleanField(default=False, verbose_name='是否已被注册'),
        ),
        migrations.AlterField(
            model_name='question',
            name='rightChoice',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C')], default=1, verbose_name='正确选项'),
        ),
    ]
