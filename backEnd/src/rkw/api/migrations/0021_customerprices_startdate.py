# Generated by Django 2.1.7 on 2019-03-26 12:21

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190325_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprices',
            name='startDate',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]
