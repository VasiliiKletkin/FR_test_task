from clients.models import Client, Message
from rest_framework.viewsets import ModelViewSet

from .serializers import ClientSerializer, MessageSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
