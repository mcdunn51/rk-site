# Generated by Django 2.1.7 on 2019-04-30 13:19

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_imagetest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Imagetest',
        ),
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=django_mysql.models.JSONField(default=dict),
        ),
    ]
