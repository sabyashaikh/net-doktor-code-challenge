from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Campaign
from .serializers import CampaignSerializer
from rest_framework import viewsets


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
