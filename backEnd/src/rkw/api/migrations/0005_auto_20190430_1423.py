# Generated by Django 2.1.7 on 2019-04-30 13:23

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190430_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=django_mysql.models.JSONField(default=dict, null=True),
        ),
    ]