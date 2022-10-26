from rest_framework import viewsets
from subestacoes.api.serializers import SubestacoesSerializer
from subestacoes.models import Subestacoes


class SubestacoesViewset(viewsets.ModelViewSet):
    serializer_class = SubestacoesSerializer

    def get_queryset(self):
        return Subestacoes.objects.all()
