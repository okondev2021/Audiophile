# Generated by Django 3.2.9 on 2022-09-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0019_cartitem_finalcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='FinalCount',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='Final_Price',
            field=models.IntegerField(default=0),
        ),
    ]
