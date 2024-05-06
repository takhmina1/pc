from rest_framework import generics
from .models import CurrencyRequest
from .serializers import CurrencyRequestSerializer

class CurrencyRequestAPIView(generics.ListAPIView):
    queryset = CurrencyRequest.objects.all()
    serializer_class = CurrencyRequestSerializer