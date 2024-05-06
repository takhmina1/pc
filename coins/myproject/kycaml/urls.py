from django.urls import path
from .views import KYCAMLCheckAPIView

urlpatterns = [
    path('kycaml-check/', KYCAMLCheckAPIView.as_view(), name='kycaml_check'),
    # Define the URL pattern for KYCAMLCheckAPIView
]
