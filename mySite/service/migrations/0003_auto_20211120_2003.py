# Generated by Django 3.2.6 on 2021-11-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default=True, max_length=11),
        ),
    ]