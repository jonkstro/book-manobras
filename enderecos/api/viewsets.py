from rest_framework import viewsets
from enderecos.api.serializers import EnderecosSerializer
from enderecos.models import Enderecos

class EnderecosViewset(viewsets.ModelViewSet):
    serializer_class=EnderecosSerializer
    def get_queryset(self):
        return Enderecos.objects.all()