# Generated by Django 2.0.3 on 2019-09-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_sicilianitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='sicilians',
        ),
    ]
