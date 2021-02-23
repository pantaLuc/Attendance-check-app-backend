from rest_framework import serializers 
from .models import Surveillant

class SurveillantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveillant
        fields = "__all__"