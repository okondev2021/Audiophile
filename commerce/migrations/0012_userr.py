# Generated by Django 3.2.9 on 2022-07-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0011_remove_product_number_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
            ],
        ),
    ]
