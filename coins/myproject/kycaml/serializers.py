from rest_framework import serializers
from .models import KYCAMLCheck
class KYCAMLCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCAMLCheck
        fields = ('title', 'text')
