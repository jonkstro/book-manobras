from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from rest_framework import routers
from core.api.viewsets import ServicosViewset
from enderecos.api.viewsets import EnderecosViewset
from equipamentos.api.viewsets import EquipamentosViewset
from manobras.api.viewsets import ManobrasViewset
from obs_equipamentos.api.viewsets import ObsEquipamentosViewset
from subestacoes.api.viewsets import SubestacoesViewset

from core.views import list_equipamentos


router = routers.DefaultRouter()

router.register('servicos', ServicosViewset, basename='Servicos')
router.register('enderecos', EnderecosViewset, basename='Enderecos')
router.register('equipamentos', EquipamentosViewset, basename='Equipamentos')
router.register('manobras', ManobrasViewset, basename='Manobras')
router.register(
    'obs-equipamentos',
    ObsEquipamentosViewset,
    basename='ObsEquipamentos'
)
router.register('subestacoes', SubestacoesViewset, basename='Subestacoes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('list-eqp/<int:se_id>', list_equipamentos, name='list_eqp')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
