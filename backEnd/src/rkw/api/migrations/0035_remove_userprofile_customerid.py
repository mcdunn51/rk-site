# Generated by Django 2.1.7 on 2019-04-08 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20190405_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='customerID',
        ),
    ]
