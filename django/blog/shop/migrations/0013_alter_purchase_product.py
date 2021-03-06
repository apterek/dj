# Generated by Django 3.2.6 on 2021-10-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_purchase_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_purchases', to='shop.product'),
        ),
    ]
