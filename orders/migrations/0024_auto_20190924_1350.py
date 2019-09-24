# Generated by Django 2.0.3 on 2019-09-24 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20190924_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size')),
            ],
        ),
        migrations.CreateModel(
            name='DinnerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Dinner')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='dinners',
            field=models.ManyToManyField(blank=True, related_name='dinners', to='orders.DinnerItem'),
        ),
    ]
