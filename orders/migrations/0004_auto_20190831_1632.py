# Generated by Django 2.0.3 on 2019-08-31 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190831_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='regular',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
    ]
