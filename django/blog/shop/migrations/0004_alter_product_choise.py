# Generated by Django 3.2.6 on 2021-09-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_choise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='choise',
            field=models.IntegerField(choices=[(1, 'router'), (2, 'switch')], default=1),
        ),
    ]