from django.contrib import admin
from .models import Contact, ChatMessage

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'website']
    search_fields = ['email']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'message', 'timestamp']
    search_fields = ['sender']
    list_filter = ['timestamp']
