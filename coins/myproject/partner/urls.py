from django.urls import path
from .views import PartnerListCreateAPIView, ReferralListCreateAPIView

urlpatterns = [
    path('partners/', PartnerListCreateAPIView.as_view(), name='partner-list-create'),
    path('referrals/', ReferralListCreateAPIView.as_view(), name='referral-list-create'),
]
