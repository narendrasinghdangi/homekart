# Generated by Django 4.0.2 on 2022-04-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='market',
            fields=[
                ('market_id', models.AutoField(primary_key=True, serialize=False)),
                ('market_name', models.CharField(default='', max_length=100)),
                ('market_state', models.CharField(default='', max_length=100)),
                ('market_city', models.CharField(default='', max_length=100)),
                ('market_items', models.CharField(default='', max_length=9000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='farmer/images')),
            ],
        ),
    ]
