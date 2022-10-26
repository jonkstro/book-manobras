from rest_framework import serializers
from subestacoes.models import Subestacoes


class SubestacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subestacoes
        fields = ('__all__')
