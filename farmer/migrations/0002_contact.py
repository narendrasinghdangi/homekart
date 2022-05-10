# Generated by Django 4.0.2 on 2022-04-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=20)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]