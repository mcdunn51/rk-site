# Generated by Django 2.1.7 on 2019-04-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20190401_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='HI',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='TI',
            field=models.IntegerField(default=0),
        ),
    ]
