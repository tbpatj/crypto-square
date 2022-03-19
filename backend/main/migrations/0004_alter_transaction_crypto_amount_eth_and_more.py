# Generated by Django 4.0.3 on 2022-03-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='crypto_amount_eth',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='crypto_txn_hash',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='crypto_uid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='exchange_amount_fiat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='exchange_sale_id',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='order_amount_fiat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='plaid_access_token',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='plaid_txn_id',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
