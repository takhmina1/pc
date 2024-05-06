from django.urls import path
from .views import BuyCryptoAPIView, SellCryptoAPIView, BuyFiatAPIView, SellFiatAPIView

urlpatterns = [
    path('buy/crypto/', BuyCryptoAPIView.as_view(), name='buy-crypto'),
    path('sell/crypto/', SellCryptoAPIView.as_view(), name='sell-crypto'),
    path('buy/fiat/', BuyFiatAPIView.as_view(), name='buy-fiat'),
    path('sell/fiat/', SellFiatAPIView.as_view(), name='sell-fiat'),
]
