# Generated by Django 4.0.4 on 2022-06-05 06:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_cart_customer_alter_cartitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AddField(
            model_name='company',
            name='account_no',
            field=models.PositiveIntegerField(default=1131164190, validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='company',
            name='bank_name',
            field=models.CharField(default='Polaris Bank Ltd.', max_length=225),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/companies/receipts'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.cart'),
        ),
    ]
