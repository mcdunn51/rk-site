# Generated by Django 2.1.7 on 2019-04-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_remove_userprofile_customerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='Code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='customerNO',
            field=models.CharField(max_length=20),
        ),
    ]