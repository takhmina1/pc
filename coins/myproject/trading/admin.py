from django.contrib import admin
from .models import Cryptocurrency, FiatCurrency, UserProfile, CryptoWallet, FiatWallet, Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'amount', 'price', 'commission', 'timestamp')
    list_filter = ('transaction_type',)

admin.site.register(Cryptocurrency)
admin.site.register(FiatCurrency)
admin.site.register(UserProfile)
admin.site.register(CryptoWallet)
admin.site.register(FiatWallet)
admin.site.register(Transaction, TransactionAdmin)
