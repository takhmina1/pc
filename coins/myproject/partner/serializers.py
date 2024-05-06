from rest_framework import serializers
from .models import Partner, Referral

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner._meta.get_field('user').related_model
        fields = ['id', 'email']
class PartnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Partner
        fields = ['id', 'user', 'referral_link']

class ReferralSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer()
    referred_user = UserSerializer()

    class Meta:
        model = Referral
        fields = ['id', 'partner', 'referred_user', 'exchange_amount']
