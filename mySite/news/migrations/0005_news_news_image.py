# Generated by Django 3.2.6 on 2021-11-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_new_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.FileField(default=None, max_length=255, null=True, upload_to='news/'),
        ),
    ]
