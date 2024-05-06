from django.urls import path
from . import views

urlpatterns = [
    path('investments/', views.InvestmentListCreateAPIView.as_view(), name='investment-list'),
    path('strategies/', views.TradingStrategyListCreateAPIView.as_view(), name='strategy-list'),
    path('trades/', views.TradeListCreateAPIView.as_view(), name='trade-list'),
]
