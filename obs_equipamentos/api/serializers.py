from rest_framework import serializers
from obs_equipamentos.models import ObsEquipamentos


class ObsEquipamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObsEquipamentos
        fields = ('__all__')
