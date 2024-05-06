from rest_framework import generics
from .models import CurrencyNews
from .serializers import CurrencyNewsSerializer

class CurrencyNewsAPIView(generics.ListAPIView):
    queryset = CurrencyNews.objects.all()
    serializer_class = CurrencyNewsSerializer