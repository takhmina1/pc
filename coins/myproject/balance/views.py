from rest_framework.views import APIView
from .models import Balance, Transac
from .serializers import BalanceSerializer, TransacSerializer
from rest_framework.response import Response
from rest_framework import generics
class BalanceAPIView(generics.ListAPIView):
    serializer_class = BalanceSerializer  # ваш сериализатор

    def get_queryset(self):
        return Balance.objects.all()

class TransactionHistoryAPIView(APIView):
    def get(self, request):
        transactions = Transac.objects.all()
        serializer = TransacSerializer(transactions, many=True)
        return Response(serializer.data)
