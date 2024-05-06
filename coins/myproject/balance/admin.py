from django.contrib import admin
from .models import Balance, Transac

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'currency', 'amount']
    search_fields = ['user__username']
    list_filter = ['currency']

@admin.register(Transac)
class TransacAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp']
    search_fields = ['user__username']
    list_filter = ['timestamp']
