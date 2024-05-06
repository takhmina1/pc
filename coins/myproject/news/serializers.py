from rest_framework import serializers
from .models import CurrencyNews

class CurrencyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyNews
        fields = ['id', 'title', 'content', 'date', 'image']
