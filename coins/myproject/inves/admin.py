from django.contrib import admin
from .models import Investment, TradingStrategy, Trade

admin.site.register(Investment)
admin.site.register(TradingStrategy)
admin.site.register(Trade)
