from rest_framework import viewsets
from core.api.serializers import ServicosSerializer
from core.models import Servicos


class ServicosViewset(viewsets.ModelViewSet):
    serializer_class = ServicosSerializer

    def get_queryset(self):
        return Servicos.objects.all()
