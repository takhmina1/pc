from django.urls import path
from .views import BalanceAPIView,TransactionHistoryAPIView

urlpatterns = [
    path('balances/', BalanceAPIView.as_view(), name='balance-list'),
    path('transactions/',TransactionHistoryAPIView.as_view(), name='transaction-list'),
]
