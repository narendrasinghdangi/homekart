# Generated by Django 4.0.2 on 2022-03-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homekart', '0002_contact_alter_productl_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=70),
        ),
    ]
