# Generated by Django 3.2.9 on 2022-06-29 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_remove_cartitem_cartname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product_Count',
            new_name='ProductCount',
        ),
    ]
