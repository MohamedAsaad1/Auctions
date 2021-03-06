# Generated by Django 4.0.5 on 2022-06-24 21:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WatchList',
        ),
        migrations.AddField(
            model_name='bids',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='bids',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.listings'),
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userb', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 21, 15, 16, 585560), null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.listings'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listings',
            name='watchList',
            field=models.ManyToManyField(blank=True, related_name='watch_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bids',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 21, 15, 16, 584444)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='name_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listings',
            name='url_image',
            field=models.URLField(blank=True),
        ),
    ]
