# Generated by Django 3.2.9 on 2022-06-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_rename_product_cartitem_productname'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='CartName',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
