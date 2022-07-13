# Generated by Django 4.0.5 on 2022-06-24 23:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_comments_date_alter_listings_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 20, 50, 995358), null=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 20, 50, 994345)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='url_image',
            field=models.URLField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/2/2f/No-photo-m.png'),
        ),
    ]
