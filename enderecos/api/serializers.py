from rest_framework import serializers
from enderecos.models import Enderecos


class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('__all__')
