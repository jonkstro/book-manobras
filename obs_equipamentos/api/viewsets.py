from rest_framework import viewsets
from obs_equipamentos.api.serializers import ObsEquipamentosSerializer
from obs_equipamentos.models import ObsEquipamentos


class ObsEquipamentosViewset(viewsets.ModelViewSet):
    serializer_class = ObsEquipamentosSerializer

    def get_queryset(self):
        return ObsEquipamentos.objects.all()
