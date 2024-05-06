from django.urls import path
from .views import ContactListCreateAPIView, ChatMessageListCreateAPIView

urlpatterns = [
    path('contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('chat-messages/', ChatMessageListCreateAPIView.as_view(), name='chatmessage-list-create'),
]
