from rest_framework import generics, status
from rest_framework.response import Response
from .models import Discount, Transaction
from .serializers import DiscountSerializer, TransactionSerializer
from .services import update_discount

class DiscountListCreateAPIView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class TransactionCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new transaction.
    """
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        """
        Override perform_create to update discount after creating transaction.
        """
        transaction = serializer.save()
        update_discount(transaction.user, transaction.amount)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
