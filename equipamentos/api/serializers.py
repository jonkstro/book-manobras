from rest_framework import serializers
from equipamentos.models import Equipamentos



class EquipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamentos
        fields = ('__all__')
