from .models import Destination
from rest_framework import serializers

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id','name','desc','price','img','offer']