# Generated by Django 3.2.6 on 2021-11-19 12:42

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
