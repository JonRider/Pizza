# Generated by Django 2.0.3 on 2019-09-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_subtopping_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subs',
            field=models.ManyToManyField(blank=True, related_name='subs', to='orders.SubItem'),
        ),
    ]
