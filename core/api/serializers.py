from rest_framework import serializers
from core.models import Servicos


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = ('__all__')
