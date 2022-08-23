from .models import Campaign
from .serializers import CampaignSerializer
from rest_framework import viewsets


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get_queryset(self):
        """
        This method filters all the campaign by the status portion of the URL if status provided.
        """
        status = self.request.query_params.get('status', None)
        if status:
            return Campaign.objects.filter(status__in=status.split(','))
        return Campaign.objects.all()
