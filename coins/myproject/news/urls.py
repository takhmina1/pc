from django.urls import path
from .views import CurrencyNewsAPIView

urlpatterns = [
    path('news/', CurrencyNewsAPIView.as_view(), name='currency-news-list'),
    ]
