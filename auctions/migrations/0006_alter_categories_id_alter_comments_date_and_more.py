# Generated by Django 4.0.5 on 2022-06-24 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_comments_date_alter_listings_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 36, 17, 636693), null=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 23, 36, 17, 635603)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]