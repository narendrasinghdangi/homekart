# Generated by Django 4.0.2 on 2022-03-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homekart', '0006_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
