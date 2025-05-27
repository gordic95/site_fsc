from django.contrib import admin
from . models import Message

class MessageAdmin(admin.ModelAdmin):
    fields = ['author_from', 'author_to', 'message', 'is_read']


admin.site.register(Message, MessageAdmin)