from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Partner, Referral
from .serializers import PartnerSerializer, ReferralSerializer

class PartnerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticated]

class ReferralListCreateAPIView(generics.ListCreateAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated]
