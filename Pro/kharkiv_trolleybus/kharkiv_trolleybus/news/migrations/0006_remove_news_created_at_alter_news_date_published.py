# Generated by Django 5.2 on 2025-05-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='news',
            name='date_published',
            field=models.DateField(),
        ),
    ]
