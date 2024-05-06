from django.contrib import admin
from .models import Partner, Referral

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'referral_link')
    search_fields = ('user__username',)
    list_filter = ('user__is_staff', 'user__is_superuser')

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referred_user', 'partner', 'exchange_amount')
    search_fields = ('referred_user__username', 'partner__user__username')
    list_filter = ('partner__user__is_staff', 'partner__user__is_superuser')
