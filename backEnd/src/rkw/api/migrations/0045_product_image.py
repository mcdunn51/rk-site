# Generated by Django 2.1.7 on 2019-04-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20190410_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
