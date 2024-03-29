# Generated by Django 2.0.3 on 2019-09-03 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_cart_sicilians'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sicilian',
            name='price_large',
        ),
        migrations.RemoveField(
            model_name='sicilian',
            name='price_small',
        ),
        migrations.AddField(
            model_name='sicilian',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sicilian',
            name='size',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
            preserve_default=False,
        ),
    ]
