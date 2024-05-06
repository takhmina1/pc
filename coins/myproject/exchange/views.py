from rest_framework import generics
from rest_framework.response import Response
from .models import ExchangeRule
from .serializers import ExchangeRuleSerializer

class ExchangeRuleListView(generics.ListAPIView):
    queryset = ExchangeRule.objects.all()
    serializer_class = ExchangeRuleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)