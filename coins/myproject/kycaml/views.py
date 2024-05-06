from rest_framework import generics
from rest_framework.response import Response
from .models import KYCAMLCheck
from .serializers import KYCAMLCheckSerializer

class KYCAMLCheckAPIView(generics.ListAPIView):
    queryset = KYCAMLCheck.objects.all()  # Fetch all KYCAMLCheck objects from the database
    serializer_class = KYCAMLCheckSerializer  # Use KYCAMLCheckSerializer for serialization

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Retrieve the queryset
        serializer = self.serializer_class(queryset, many=True)  # Serialize the queryset
        return Response(serializer.data)  # Return the serialized data in the response
