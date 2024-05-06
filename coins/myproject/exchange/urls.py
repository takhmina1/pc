from django.urls import path
from .views import ExchangeRuleListView

urlpatterns = [
    path('exchange/', ExchangeRuleListView.as_view(), name='exchange-rule-list-create'),
]
