# Generated by Django 2.0.6 on 2018-07-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180630_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantNaive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
