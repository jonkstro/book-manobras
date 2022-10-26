from pyexpat import model
from rest_framework import serializers
from manobras.models import Manobras


class ManobrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manobras
        fields = ('__all__')
