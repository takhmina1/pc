from rest_framework.response import Response
from rest_framework import status, generics
from .models import Review
from .serializers import ReviewSerializer
class ReviewList(generics.ListCreateAPIView):
    """
    Бардык жарандарды тизмелеп көрсөтүп, же жаңы барактарды кошуңуз.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
