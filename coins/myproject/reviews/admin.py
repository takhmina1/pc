from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_posted')  # Customize what fields to display in the admin list view
    search_fields = ('author', 'content')  # Add fields for searching
    list_filter = ('date_posted',)  # Add filters for date_posted

admin.site.register(Review, ReviewAdmin)
