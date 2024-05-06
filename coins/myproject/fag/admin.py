from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = 'title', 'text'  # Remove the parentheses here
    search_fields = 'title', 'text'  # Remove the parentheses here
    list_filter = 'title', 'text'  # Remove the parentheses here
