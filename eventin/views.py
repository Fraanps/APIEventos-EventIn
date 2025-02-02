from django.http import JsonResponse

def participantes(request):
    if request.method == 'GET':
        participante = {
            "id": 1,
            "nome": "Fulano"
        }
        return JsonResponse(participante)


