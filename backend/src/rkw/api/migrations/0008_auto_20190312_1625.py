# Generated by Django 2.1.7 on 2019-03-12 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_product_ipgid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipg',
            old_name='Code',
            new_name='ItemID',
        ),
    ]