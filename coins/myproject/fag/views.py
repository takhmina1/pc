from rest_framework.response import Response
from .serializers import FAQSerializer
from .models import FAQ
from rest_framework import generics

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FAQSerializer(queryset, many=True)
        return Response(serializer.data)
