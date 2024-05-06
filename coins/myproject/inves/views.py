from rest_framework import generics
from .models import Investment, TradingStrategy
from .serializers import InvestmentSerializer, TradingStrategySerializer, TradeSerializer
from .services import TradeService

class InvestmentListCreateAPIView(generics.ListAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class TradingStrategyListCreateAPIView(generics.ListCreateAPIView):
    queryset = TradingStrategy.objects.all()
    serializer_class = TradingStrategySerializer

class TradeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TradeSerializer

    def get_queryset(self):
        """
        Optionally, you might want to override get_queryset to filter trades based on user.
        """
        user = self.request.user  # Assuming you're using authentication
        return TradeService.get_trades_by_user(user)

    def perform_create(self, serializer):
        """
        Override perform_create to customize creation logic.
        """
        user = self.request.user
        investment_id = serializer.validated_data.get('investment_id')
        amount = serializer.validated_data.get('amount')
        trade = TradeService.create_trade(user, investment_id, amount)
        serializer.instance = trade
