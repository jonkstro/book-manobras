from rest_framework import viewsets
from manobras.api.serializers import ManobrasSerializer
from manobras.models import Manobras


class ManobrasViewset(viewsets.ModelViewSet):
    serializer_class = ManobrasSerializer

    def get_queryset(self):
        return Manobras.objects.all()
