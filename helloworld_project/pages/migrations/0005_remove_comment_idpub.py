# Generated by Django 3.1.3 on 2020-11-23 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201123_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='idPub',
        ),
    ]
