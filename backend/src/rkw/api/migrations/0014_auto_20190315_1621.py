# Generated by Django 2.1.7 on 2019-03-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190315_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipg',
            name='Code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ipg',
            name='Description',
            field=models.CharField(max_length=20),
        ),
    ]
