from django.urls import path
from .views import CurrencyRequestAPIView
urlpatterns = [
    path('currency/', CurrencyRequestAPIView.as_view(), name='currency-request-list'),
   ]
