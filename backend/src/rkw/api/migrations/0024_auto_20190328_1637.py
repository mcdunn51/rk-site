# Generated by Django 2.1.7 on 2019-03-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_userprofile_customerno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='companyName',
            field=models.CharField(max_length=50),
        ),
    ]