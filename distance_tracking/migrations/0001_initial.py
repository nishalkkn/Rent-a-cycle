# Generated by Django 3.2.21 on 2024-02-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceTracking',
            fields=[
                ('distance_tracking_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_point', models.CharField(max_length=45)),
                ('end_point', models.CharField(max_length=45)),
                ('distance', models.FloatField()),
            ],
            options={
                'db_table': 'distance_tracking',
                'managed': False,
            },
        ),
    ]
