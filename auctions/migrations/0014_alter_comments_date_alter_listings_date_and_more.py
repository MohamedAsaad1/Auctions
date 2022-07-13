# Generated by Django 4.0.5 on 2022-06-28 21:26

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_comments_date_alter_listings_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 21, 26, 23, 568324), null=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 21, 26, 23, 567307)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='watchList',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]