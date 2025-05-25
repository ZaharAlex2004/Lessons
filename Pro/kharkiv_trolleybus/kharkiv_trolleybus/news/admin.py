from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(UploadFiles)
admin.site.register(UploadVideoFile)
