# Generated by Django 2.2.4 on 2019-08-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
