from rest_framework import serializers
from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    start = serializers.DateField(format="%d-%m-%Y")
    end = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = Campaign
        fields = ["cs_id", "customer", "name", "start", "end", "status", "note"]
