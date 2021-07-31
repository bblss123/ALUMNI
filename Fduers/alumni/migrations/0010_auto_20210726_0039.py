# Generated by Django 3.2.5 on 2021-07-26 00:39

from django.db import migrations, models




class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0009_auto_20210725_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvinceID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='省份')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='/static/img/default.jpg', null=True, upload_to='user_photo/%Y/%m/%d', verbose_name='头像'),
        ),
    ]