# Generated by Django 4.0.5 on 2022-06-24 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_delete_watchlist_bids_amount_bids_item_bids_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 21, 16, 7, 169668), null=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 21, 16, 7, 168633)),
        ),
    ]
