# Generated by Django 3.2.9 on 2022-07-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0015_cartitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='Total',
            field=models.IntegerField(default=0),
        ),
    ]
