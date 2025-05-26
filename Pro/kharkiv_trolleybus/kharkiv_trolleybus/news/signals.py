from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import News
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

@receiver(post_save, sender=News)
def send_new_news_to_websocket(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "news_group",
            {
                'type': 'send_news',
                'news': {
                    'title': instance.title,
                    'sourse': instance.sourse,
                    'date_published': instance.date_published.strftime('%Y-%m-%d'),
                    'content': instance.content,
                    'author': instance.author.username if instance.author else None,
                }
            }
        )
