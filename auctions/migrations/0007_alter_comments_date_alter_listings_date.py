# Generated by Django 4.0.5 on 2022-06-25 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_categories_id_alter_comments_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 19, 9, 38, 962484), null=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 19, 9, 38, 961488)),
        ),
    ]
