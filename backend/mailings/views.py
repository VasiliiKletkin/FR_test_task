from clients.models import Message
from clients.serializers import MessageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Mailing
from .serializers import MailingSerializer


class MailingViewSet(ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(detail=True, methods=["get"])
    def info(self, request, pk=None):
        """
        Summary data for a specific mailing list
        """
        queryset_mailing = Mailing.objects.all()
        get_object_or_404(queryset_mailing, pk=pk)
        queryset = Message.objects.filter(mailing_id=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def fullinfo(self, request):
        """
        Summary data for all mailings
        """
        total_count = Mailing.objects.count()
        mailing = Mailing.objects.values("id")
        content = {
            "Total number of mailings": total_count,
            "The number of messages sent": "",
        }
        result = {}

        for row in mailing:
            mail = Message.objects.filter(mailing_id=row["id"]).all()
            group_sent = mail.filter(sending_status="Sent").count()
            group_no_sent = mail.filter(sending_status="No sent").count()
            res = {
                "Total messages": len(mail),
                "Sent": group_sent,
                "No sent": group_no_sent,
            }
            result[row["id"]] = res

        content["The number of messages sent"] = result
        return Response(content)
