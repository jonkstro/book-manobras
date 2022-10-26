from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from equipamentos.models import Equipamentos
from subestacoes.models import Subestacoes

def list_equipamentos(request, se_id):
    data = Subestacoes.objects.filter(id=se_id).get()
    i = data.equipamento.all()
    return HttpResponse(i)
    # return JsonResponse(['a', 'b'], safe=False)



# for d in user.device.all():
#   print(d.dev_id)



# def list_actors( request, programme_id):
#     programme = Programme.objects.filter(id = programme_id)[0]
#     actors = Actor.objects.filter(programme = programme_id)
#     json = simplejson.dumps( [{
#         'name': str(actor.name),
#         'rating': str(actor.rating),} for actor in actors] )
#     return HttpResponse(json, mimetype='application/javascript')
