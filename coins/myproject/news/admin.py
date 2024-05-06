from django.contrib import admin
from .models import CurrencyNews

@admin.register(CurrencyNews)
class CurrencyNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    search_fields = ['title', 'content']
    list_filter = ['date']
