from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kharkiv_trolleybus.settings')

app = Celery('kharkiv_trolleybus')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['news'])

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
