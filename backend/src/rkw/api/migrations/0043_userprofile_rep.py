# Generated by Django 2.1.7 on 2019-04-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_product_analysis1'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rep',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
