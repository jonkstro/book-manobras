from rest_framework import viewsets
from equipamentos.api.serializers import EquipamentosSerializer
from equipamentos.models import Equipamentos


class EquipamentosViewset(viewsets.ModelViewSet):
    serializer_class = EquipamentosSerializer

    def get_queryset(self):
        return Equipamentos.objects.all()
