from django.contrib import admin
from .models import Discount, Transaction

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_transactions', 'discount_percentage']
    fieldsets = (
        (None, {
            'fields': ('user', 'total_transactions', 'discount_percentage'),
        }),
    )

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp']
    fieldsets = (
        (None, {
            'fields': ('user', 'amount'),
        }),
    )
