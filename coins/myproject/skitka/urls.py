from django.urls import path
from . import views

urlpatterns = [
    path('discounts/', views.DiscountListCreateAPIView.as_view(), name='discount-list'),
    path('transactions/', views.TransactionCreateView.as_view(), name='transaction-list'),
]
