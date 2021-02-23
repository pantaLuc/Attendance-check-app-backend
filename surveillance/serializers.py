from rest_framework import serializers 
from .models import Surveillant, Salle

class SurveillantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveillant
        fields = "__all__"


class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = "__all__"